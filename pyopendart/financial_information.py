from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Dict, Optional, Sequence, Tuple

from pyopendart.client import DartClient
from pyopendart.common import ReportType, dart_atoi, is_dart_null


class FinancialStatementType(Enum):
    INCOME_STATEMENT = "IS"
    BALANCE_SHEET = "BS"
    COMPREHENSIVE_INCOME_STATEMENT = "CIS"
    CASH_FLOW = "CF"
    EQUITY_CHANGE_STATEMENT = "SCE"


@dataclass(frozen=True)
class Account:
    receipt_no: str  # rcept_no
    business_year: int  # bsns_year
    corporation_code: str  # corp_code
    ticker: str  # stock_code
    report_type: ReportType  # reprt_code

    title: str  # account_nm
    is_consolidated: bool  # fs_div, fs_nm
    financial_statement_type: FinancialStatementType  # sj_div, sj_nm

    @dataclass(frozen=True)
    class TermData:
        name: str
        date: str
        amount: int

    current_term: TermData  # thstrm_nm, thstrm_dt, thstrm_amount
    prev_term: TermData  # frmtrm_nm, frmtrm_dt, frmtrm_amount
    prev_prev_term: TermData  # bfefrmtrm_nm, bfefrmtrm_dt, bfefrmtrm_amount

    order: int

    @staticmethod
    def from_dart_resp(resp):
        return Account(
            receipt_no=resp.get("rcept_no"),
            business_year=int(resp.get("bsns_year")),
            corporation_code=resp.get("corp_code"),
            ticker=resp.get("stock_code"),
            report_type=ReportType(int(resp.get("reprt_code"))),
            title=resp.get("account_nm"),
            is_consolidated=True if resp.get("fs_div") == "CFS" else False,
            financial_statement_type=FinancialStatementType(resp.get("sj_div")),
            current_term=Account.TermData(
                name=resp.get("thstrm_nm"),
                date=resp.get("thstrm_dt"),
                amount=dart_atoi(resp.get("thstrm_amount")),
            ),
            prev_term=Account.TermData(
                name=resp.get("frmtrm_nm"),
                date=resp.get("frmtrm_dt"),
                amount=dart_atoi(resp.get("frmtrm_amount")),
            ),
            prev_prev_term=Account.TermData(
                name=resp.get("bfefrmtrm_nm"),
                date=resp.get("bfefrmtrm_dt"),
                amount=dart_atoi(resp.get("bfefrmtrm_amount")),
            ),
            order=dart_atoi(resp.get("ord")),
        )


@dataclass(frozen=True)
class DetailedAccount(Account):
    id: str
    detail: str

    @dataclass(frozen=True)
    class TermData:
        name: str
        date: str
        amount: Optional[int]

    current_term: TermData
    prev_term: TermData
    prev_prev_term: TermData

    @staticmethod
    def from_dart_resp(resp):
        return DetailedAccount(
            receipt_no=resp.get("rcept_no"),
            business_year=int(resp.get("bsns_year")),
            corporation_code=resp.get("corp_code"),
            ticker=resp.get("stock_code"),
            report_type=ReportType(int(resp.get("reprt_code"))),
            id=resp.get("account_id"),
            title=resp.get("account_nm"),
            detail=resp.get("account_detail"),
            is_consolidated=True if resp.get("fs_div") == "CFS" else False,
            financial_statement_type=FinancialStatementType(resp.get("sj_div")),
            current_term=DetailedAccount.TermData(
                name=resp.get("thstrm_nm"),
                date=resp.get("thstrm_dt"),
                amount=dart_atoi(resp["thstrm_amount"]) if not is_dart_null(resp.get("thstrm_amount")) else None,
            ),
            prev_term=DetailedAccount.TermData(
                name=resp.get("frmtrm_nm"),
                date=resp.get("frmtrm_dt"),
                amount=dart_atoi(resp["frmtrm_amount"]) if not is_dart_null(resp.get("frmtrm_amount")) else None,
            ),
            prev_prev_term=DetailedAccount.TermData(
                name=resp.get("bfefrmtrm_nm"),
                date=resp.get("bfefrmtrm_dt"),
                amount=dart_atoi(resp["bfefrmtrm_amount"]) if not is_dart_null(resp.get("bfefrmtrm_amount")) else None,
            ),
            order=dart_atoi(resp.get("ord")),
        )


@dataclass(frozen=True)
class XbrlTaxonomy:
    id: str  # account_id
    title: str  # account_nm
    base_date: date  # bsns_de
    detailed_financial_statement_type: str  # sj_div

    @dataclass(frozen=True)
    class Label:
        ko: str  # label_kor
        en: str  # label_eng

    label: Label
    format: Optional[str]  # data_tp
    ifrs_ref: str  # ifrs_ref

    @staticmethod
    def from_dart_resp(resp):
        return XbrlTaxonomy(
            id=resp.get("account_id"),
            title=resp.get("account_nm"),
            base_date=datetime.strptime(resp.get("bsns_de"), "%Y%m%d").date(),
            detailed_financial_statement_type=resp.get("sj_div"),
            label=XbrlTaxonomy.Label(
                ko=resp.get("label_kor"),
                en=resp.get("label_eng"),
            ),
            format=resp.get("data_tp"),
            ifrs_ref=resp.get("ifrs_ref"),
        )


class FinancialInformation:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_financial_statements_of_major_accounts(
        self, corporation_code: Sequence[str], business_year: int, report_type: ReportType
    ) -> Dict[str, Tuple[Account]]:
        if len(corporation_code) == 0:
            return {}
        elif len(corporation_code) == 1:
            params = {
                "corp_code": corporation_code[0],
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            resp = self.client.json("fnlttSinglAcnt", **params)

            accounts = [Account.from_dart_resp(i) for i in resp.get("list", [])]
            accounts.sort(key=lambda v: v.order)
            accounts = tuple(accounts)

            return {corporation_code[0]: accounts}
        else:
            params = {
                "corp_code": ','.join(corporation_code),
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            resp = self.client.json("fnlttMultiAcnt", **params)

            accounts = [Account.from_dart_resp(i) for i in resp.get("list", [])]
            grouped_accounts = {}

            for corp in corporation_code:
                accounts_filtered_by_corp = [i for i in accounts if i.corporation_code == corp]
                accounts_filtered_by_corp.sort(key=lambda v: v.order)
                grouped_accounts[corp] = tuple(accounts_filtered_by_corp)

            return grouped_accounts

    def get_full_financial_statements(
        self, corporation_code: str, business_year: int, report_type: ReportType, is_consolidated: bool = True
    ) -> Tuple[DetailedAccount]:
        params = {
            "corp_code": corporation_code,
            "bsns_year": str(business_year),
            "reprt_code": report_type.value,
            "fs_div": "CFS" if is_consolidated else "OFS",
        }
        resp = self.client.json("fnlttSinglAcntAll", **params)

        return tuple(DetailedAccount.from_dart_resp(i) for i in resp.get("list", []))

    def get_xbrl_taxonomies(self, detailed_financial_statement_type: str) -> Tuple[XbrlTaxonomy]:
        params = {"sj_div": detailed_financial_statement_type}
        resp = self.client.json("xbrlTaxonomy", **params)

        return tuple(XbrlTaxonomy.from_dart_resp(i) for i in resp.get("list", []))
