from typing import Optional, Sequence

from pyopendart.api.dataframe.business_report import BusinessReportApi as DfBusinessReportApi
from pyopendart.enums import RenameMode, ReportType


class BusinessReportApi(DfBusinessReportApi):
    def get_changes_in_equity(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_changes_in_equity(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_dividend_info(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_dividend_info(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_treasury_shares_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_treasury_shares_status(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_major_shareholders(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_major_shareholders(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_changes_in_major_shareholder(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_changes_in_major_shareholder(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_minority_shareholders_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_minority_shareholders_status(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_executives(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_executives(corporation_code, business_year, report_type, rename=rename)
        return df.to_dict("records")

    def get_employment_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_employment_status(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_individual_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_individual_executive_compensation_status(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_executive_compensation_status(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_top_5_individual_executive_compensation(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_top_5_individual_executive_compensation(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_investment_in_other_corporations(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(BusinessReportApi, self).get_investment_in_other_corporations(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")
