from dataclasses import dataclass
from enum import Enum
from typing import Dict, Sequence, Tuple

from pyopendart.client import DartClient
from pyopendart.common import ReportType, dart_atoi


class FinancialStatementType(Enum):
    INCOME_STATEMENT = "IS"
    BALANCE_SHEET = "BS"


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

    def get_all_financial_statements(self):
        pass
