from typing import Sequence

from pyopendart.clients.base import ClientBase
from pyopendart.enums import ReportType


class BusinessReportClient(ClientBase):
    def get_changes_in_equity(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("irdsSttus", params).get("list", [])

    def get_dividend_info(self, corporation_code: str, business_year: int, report_type: ReportType) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        items = self.client.xml("alotMatter", params).get("list", [])

        # polyfill
        for d in items:
            if not d.get("stock_knd"):
                d["stock_knd"] = ""

        return items

    def get_treasury_shares_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("tesstkAcqsDspsSttus", params).get("list", [])

    def get_major_shareholders(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("hyslrSttus", params).get("list", [])

    def get_changes_in_major_shareholder(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("hyslrChgSttus", params).get("list", [])

    def get_minority_shareholders_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("mrhlSttus", params).get("list", [])

    def get_executives(self, corporation_code: str, business_year: int, report_type: ReportType) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.json("exctvSttus", params).get("list", [])

    def get_employment_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("empSttus", params).get("list", [])

    def get_individual_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("hmvAuditIndvdlBySttus", params).get("list", [])

    def get_executive_compensation_status(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("hmvAuditAllSttus", params).get("list", [])

    def get_top_5_individual_executive_compensation(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("indvdlByPay", params).get("list", [])

    def get_investment_in_other_corporations(
        self, corporation_code: str, business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}
        return self.client.xml("otrCprInvstmntSttus", params).get("list", [])
