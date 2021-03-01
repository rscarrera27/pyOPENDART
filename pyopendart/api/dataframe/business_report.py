from typing import Optional

import pandas as pd

from pyopendart.api.base import ApiBase
from pyopendart.api.const import RENAME_MAPPINGS
from pyopendart.api.dataframe.utils import (
    convert_known_date_fields,
    convert_known_numeric_fields,
    convert_known_ratio_fields,
    rename_fields,
)
from pyopendart.enums import RenameMode, ReportType


class BusinessReportApi(ApiBase):
    def _dispatch_business_report(
        self,
        resource_name: str,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        params = {"corp_code": corporation_code, "bsns_year": str(business_year), "reprt_code": report_type.value}

        df = pd.DataFrame(i for i in self.client.iter_list_resource(resource_name, params))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df

    def get_changes_in_equity(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("irdsSttus", corporation_code, business_year, report_type, rename=rename)

    def get_dividend_info(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("alotMatter", corporation_code, business_year, report_type, rename=rename)

    def get_treasury_shares_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "tesstkAcqsDspsSttus", corporation_code, business_year, report_type, rename=rename
        )

    def get_major_shareholders(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("hyslrSttus", corporation_code, business_year, report_type, rename=rename)

    def get_changes_in_major_shareholder(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "hyslrChgSttus", corporation_code, business_year, report_type, rename=rename
        )

    def get_minority_shareholders_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("mrhlSttus", corporation_code, business_year, report_type, rename=rename)

    def get_executives(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("exctvSttus", corporation_code, business_year, report_type, rename=rename)

    def get_employment_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report("empSttus", corporation_code, business_year, report_type, rename=rename)

    def get_individual_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "hmvAuditIndvdlBySttus", corporation_code, business_year, report_type, rename=rename
        )

    def get_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "hmvAuditAllSttus", corporation_code, business_year, report_type, rename=rename
        )

    def get_top_5_individual_executive_compensation(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "indvdlByPay", corporation_code, business_year, report_type, rename=rename
        )

    def get_investment_in_other_corporations(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        return self._dispatch_business_report(
            "otrCprInvstmntSttus", corporation_code, business_year, report_type, rename=rename
        )


if __name__ == '__main__':
    print(dir(BusinessReportApi))
