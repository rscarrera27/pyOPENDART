from typing import Optional, Tuple

import pandas as pd

from pyopendart.clients.dataframe.utils import DEFAULT_RENAME_MAPPING, construct_dataframe, get_converters
from pyopendart.clients.namedtuple.business_report import NamedtupleBusinessReportClient
from pyopendart.enums import ReportType


class DataframeBusinessReportClient(NamedtupleBusinessReportClient):
    @staticmethod
    def _get_metadata_cols(rename: bool):
        return (
            ["receipt_no", "market", "corporation_code", "corporation_name"]
            if rename
            else ["rcept_no", "corp_cls", "corp_code", "corp_name"]
        )

    def get_changes_in_equity(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_changes_in_equity(
            corporation_code, business_year, report_type
        )
        converters = (
            get_converters(
                "corp_cls", "isu_dcrs_de", "isu_dcrs_qy", "isu_dcrs_mstvdv_fval_amount", "isu_dcrs_mstvdv_amount"
            )
            if convert_data
            else None
        )
        sort_by = ["isu_dcrs_de"]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        index = DEFAULT_RENAME_MAPPING["isu_dcrs_de"] if rename_fields else ["isu_dcrs_de"]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, sort_by=sort_by, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_dividend_info(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_dividend_info(
            corporation_code, business_year, report_type
        )

        converters = get_converters("corp_cls", "thstrm", "frmtrm", "lwfr") if convert_data else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["se", "stock_knd"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_treasury_shares_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_treasury_shares_status(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters("corp_cls", "bsis_qy", "change_qy_acqs", "change_qy_dsps", "change_qy_incnr", "trmend_qy")
            if convert_data
            else None
        )
        sort_by = [
            'acqs_mth1',
            'acqs_mth2',
            'acqs_mth3',
            'stock_knd',
        ]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        index = ["acqs_mth1", "acqs_mth2", "acqs_mth3", "stock_knd"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        df, meta = construct_dataframe(
            items, converters=converters, sort_by=sort_by, metadata_cols=metadata_cols, rename=rename, index=index
        )

        return df, meta

    def get_major_shareholders(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_major_shareholders(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters(
                "corp_cls",
                "bsis_posesn_stock_co",
                "bsis_posesn_stock_qota_rt",
                "trmend_posesn_stock_co",
                "trmend_posesn_stock_qota_rt",
            )
            if convert_data
            else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["nm", "relate"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_changes_in_major_shareholder(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_changes_in_major_shareholder(
            corporation_code, business_year, report_type
        )

        converters = get_converters("corp_cls", "posesn_stock_co", "qota_rt", "change_on") if convert_data else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["change_on"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_minority_shareholders_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_minority_shareholders_status(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters(
                "corp_cls",
                "shrholdr_co",
                "shrholdr_tot_co",
                "shrholdr_rate",
                "hold_stock_co",
                "stock_tot_co",
                "hold_stock_rate",
            )
            if convert_data
            else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["se"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_executives(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_executives(corporation_code, business_year, report_type)

        converters = get_converters("corp_cls", "rgist_exctv_at", "fte_at", "tenure_end_on") if convert_data else None
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        index = ["nm"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_employment_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_employment_status(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters(
                "corp_cls",
                "reform_bfe_emp_co_rgllbr",
                "reform_bfe_emp_co_cnttk",
                "reform_bfe_emp_co_etc",
                "rgllbr_co",
                "rgllbr_abacpt_labrr_co",
                "cnttk_co",
                "cnttk_abacpt_labrr_co",
                "sm",
                "fyer_salary_totamt",
                "jan_salary_am",
            )
            if convert_data
            else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        sort_by = ["fo_bbm", "sexdstn"]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["fo_bbm", "sexdstn"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, sort_by=sort_by, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_individual_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_individual_executive_compensation_status(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters("corp_cls", "mendng_totamt", "mendng_totamt_ct_incls_mendng") if convert_data else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["nm"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_executive_compensation_status(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_executive_compensation_status(
            corporation_code, business_year, report_type
        )

        converters = get_converters("corp_cls", "nmpr", "mendng_totamt", "jan_avrg_mendng_am") if convert_data else None
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        return construct_dataframe(items, converters=converters, metadata_cols=metadata_cols, rename=rename)

    def get_top_5_individual_executive_compensation(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_top_5_individual_executive_compensation(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters("corp_cls", "mendng_totamt", "mendng_totamt_ct_incls_mendng") if convert_data else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["nm"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )

    def get_investment_in_other_corporations(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeBusinessReportClient, self).get_investment_in_other_corporations(
            corporation_code, business_year, report_type
        )

        converters = (
            get_converters(
                "corp_cls",
                "frst_acqs_de",
                "frst_acqs_amount",
                "frst_acqs_amount",
                "bsis_blce_qy",
                "bsis_blce_qota_rt",
                "bsis_blce_acntbk_amount",
                "incrs_dcrs_acqs_dsps_qy",
                "incrs_dcrs_acqs_dsps_amount",
                "incrs_dcrs_evl_lstmn",
                "trmend_blce_qy",
                "trmend_blce_qota_rt",
                "trmend_blce_acntbk_amount",
                "recent_bsns_year_fnnr_sttus_tot_assets",
                "recent_bsns_year_fnnr_sttus_thstrm_ntpf",
            )
            if convert_data
            else None
        )
        metadata_cols = self._get_metadata_cols(rename_fields)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        index = ["inv_prm"]
        if rename:
            index = [DEFAULT_RENAME_MAPPING[k] for k in index]
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, rename=rename, index=index
        )
