import locale
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional, Tuple

from dateutil.parser import parse as datetime_parse

from pyopendart.client import DartClient
from pyopendart.common import Market


class ReportCode(Enum):
    Q1 = 11013  # 1분기보고서
    Q2 = 11012  # 반기보고서
    Q3 = 11014  # 3분기보고서
    Q4 = 11011  # 사업보고서


def dart_atoi(a: str) -> int:
    return int(a.replace(",", ""))


@dataclass(frozen=True)
class CapitalVariation:
    receipt_no: str  # rcept_no
    market: Market  # corp_cls
    corporation_code: str  # corp_code
    corporation_name: str  # corp_name
    date: date  # stock_isu_dcrs_de
    title: str  # isu_dcrs_stle
    stock_type: str  # isu_dcrs_stock_knd
    quantity: int  # isu_dcrs_qy
    face_value: int  # isu_dcrs_mstvdv_fval_amount
    issue_price: int  # isu_dcrs_mstvdv_amount

    @staticmethod
    def from_dart_resp(resp):
        return CapitalVariation(
            receipt_no=resp.get("rcept_no"),
            market=Market(resp.get("corp_cls")),
            corporation_code=resp.get("corp_code"),
            corporation_name=resp.get("corp_name"),
            date=datetime_parse(resp["stock_isu_dcrs_de"]) if resp.get("stock_isu_dcrs_de") else None,
            title=resp.get("isu_dcrs_stle"),
            stock_type=resp.get("isu_dcrs_stock_knd"),
            quantity=dart_atoi(resp.get("isu_dcrs_qy")),
            face_value=dart_atoi(resp.get("isu_dcrs_mstvdv_fval_amount")),
            issue_price=dart_atoi(resp.get("isu_dcrs_mstvdv_amount")),
        )


class BusinessReports:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def get_capital_variation(
        self, corporation_code: str, business_year: int, report_code: ReportCode
    ) -> Tuple[CapitalVariation]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_code.value}
        resp = self.client.json("irdsSttus", **params)

        if not resp.get("list"):
            return tuple()
        if len(resp.get("list")) == 1 and resp["list"][0].get("isu_dcrs_qy") == "-":
            return tuple()

        return tuple(CapitalVariation.from_dart_resp(i) for i in resp.get("list", []))

    def get_dividend_info(self):
        pass

    def get_treasury_shares_status(self):
        pass

    def get_major_shareholders_status(self):
        pass

    def get_changes_in_major_shareholders(self):
        pass

    def get_minority_shareholders_status(self):
        pass

    def get_directors(self):
        pass

    def get_employee_status(self):
        pass

    def get_individual_executive_compensation_status(self):
        pass

    def get_executive_compensation_status(self):
        pass

    def get_top_5_individual_executive_compensation(self):
        pass

    def get_investment_in_other_corporations(self):
        pass
