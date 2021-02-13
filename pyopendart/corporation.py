from typing import Any, Optional, Tuple, Type

import pandas as pd

from pyopendart.clients import (
    DataframeBusinessReportClient,
    DataframeDisclosureClient,
    DataframeFinancialInformationClient,
    DataframeShareholderReportClient,
)
from pyopendart.clients.http import OpenApiClient, RequestsOpenApiClient
from pyopendart.enums import ReportType


class Corporation:
    def __init__(
        self,
        corporation_code: str,
        api_key: str,
        client: OpenApiClient = None,
        client_cls: Type[OpenApiClient] = RequestsOpenApiClient,
        default_timeout: Any = None,
        default_download_timeout: Any = None,
        **kwargs,
    ) -> None:
        client = client or client_cls(api_key, default_timeout, default_download_timeout, **kwargs)
        self._disclosure_cli = DataframeDisclosureClient(api_key=api_key, client=client)
        self._business_report_cli = DataframeBusinessReportClient(api_key=api_key, client=client)
        self._financial_report_cli = DataframeFinancialInformationClient(api_key=api_key, client=client)
        self._shareholder_report_cli = DataframeShareholderReportClient(api_key=api_key, client=client)

        self.corporation_code = corporation_code
        self._company_info: dict = None  # noqa

    @property
    def company_info(self) -> dict:
        if self._company_info:
            return self._company_info

        df, _ = self._disclosure_cli.get_company_overview(self.corporation_code)
        self._company_info = df.iloc[0].to_dict()

        return self._company_info

    @property
    def name(self) -> dict:
        names = {
            "ko": self.company_info["corporation_name"],
            "en": self.company_info["corporation_name_en"],
            "stock": self.company_info["stock_name"],
        }
        return names

    @property
    def market_info(self) -> dict:
        market_info = {
            "name": self.company_info["stock_name"],
            "code": self.company_info["stock_code"],
            "market": self.company_info["market"],
        }
        return market_info

    def get_changes_in_equity(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_changes_in_equity(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_dividend_info(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_dividend_info(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_treasury_shares_status(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_treasury_shares_status(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_major_shareholders(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_major_shareholders(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_changes_in_major_shareholder(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_major_shareholders(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_minority_shareholders_status(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_minority_shareholders_status(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_executives(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_executives(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_employment_status(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_employment_status(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_individual_executive_compensation_status(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_individual_executive_compensation_status(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_executive_compensation_status(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_executive_compensation_status(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
        )

    def get_top_5_individual_executive_compensation(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_top_5_individual_executive_compensation(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_investment_in_other_corporations(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._business_report_cli.get_investment_in_other_corporations(
            self.corporation_code,
            business_year,
            report_type,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_financial_statements_of_major_accounts(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        force_account_order: bool = False,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._financial_report_cli.get_financial_statements_of_major_accounts(
            [self.corporation_code],
            business_year,
            report_type,
            force_account_order=force_account_order,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_full_financial_statements(
        self,
        business_year: int,
        report_type: ReportType,
        *,
        force_account_order: bool = False,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._financial_report_cli.get_full_financial_statements(
            self.corporation_code,
            business_year,
            report_type,
            force_account_order=force_account_order,
            convert_data=convert_data,
            rename_fields=rename_fields,
            set_index=set_index,
        )

    def get_major_shareholder_reports(
        self, *, convert_data: bool = True, rename_fields: bool = True, set_index: bool = True
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._shareholder_report_cli.get_major_shareholder_reports(
            self.corporation_code, convert_data=convert_data, rename_fields=rename_fields, set_index=set_index
        )

    def get_executive_shareholder_reports(
        self, *, convert_data: bool = True, rename_fields: bool = True, set_index: bool = True
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        return self._shareholder_report_cli.get_executive_shareholder_reports(
            self.corporation_code, convert_data=convert_data, rename_fields=rename_fields, set_index=set_index
        )
