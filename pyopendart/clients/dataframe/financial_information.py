from typing import Optional, Sequence, Tuple

import pandas as pd

from pyopendart.clients.dataframe.utils import DEFAULT_RENAME_MAPPING, construct_dataframe, get_converters
from pyopendart.clients.namedtuple.financial_information import NamedtupleFinancialInformationClient
from pyopendart.enums import FinancialStatementDivision, ReportType


class DataframeFinancialInformationClient(NamedtupleFinancialInformationClient):
    def get_financial_statements_of_major_accounts(
        self,
        corporation_codes: Sequence[str],
        business_year: int,
        report_type: ReportType,
        *,
        force_account_order: bool = False,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeFinancialInformationClient, self).get_financial_statements_of_major_accounts(
            corporation_codes, business_year, report_type
        )

        converters = (
            get_converters(
                "reprt_code",
                "bsns_year",
                "fs_div",
                "sj_div",
                "thstrm_amount",
                "thstrm_add_amount",
                "frmtrm_amount",
                "frmtrm_add_amount",
                "bfefrmtrm_amount",
                "ord",
            )
            if convert_data
            else None
        )
        sort_by = (
            ["rcept_no", "corp_code", "stock_code", "ord"]
            if force_account_order
            else ["rcept_no", "corp_code", "stock_code", "sj_div", "fs_div", "ord"]
        )
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        metadata_cols = ["reprt_code", "bsns_year"]
        metadata_cols = [DEFAULT_RENAME_MAPPING[c] for c in metadata_cols] if rename_fields else metadata_cols

        index = ["rcept_no", "corp_code", "stock_code", "sj_div", "sj_nm", "fs_div", "fs_nm", "account_nm"]
        index = [DEFAULT_RENAME_MAPPING[i] for i in index] if rename_fields else index
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, sort_by=sort_by, rename=rename, index=index
        )

    def get_full_financial_statements(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        financial_statement_division: FinancialStatementDivision = FinancialStatementDivision.FINANCIAL_STATEMENT,
        *,
        force_account_order: bool = False,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeFinancialInformationClient, self).get_full_financial_statements(
            corporation_code, business_year, report_type, financial_statement_division
        )

        converters = (
            get_converters(
                "reprt_code",
                "bsns_year",
                "sj_div",
                "thstrm_amount",
                "frmtrm_amount",
                "frmtrm_q_amount",
                "bfefrmtrm_amount",
                "ord",
            )
            if convert_data
            else None
        )
        sort_by = ["ord"] if force_account_order else ["sj_div", "ord"]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        metadata_cols = ["rcept_no", "reprt_code", "bsns_year", "corp_code"]
        metadata_cols = [DEFAULT_RENAME_MAPPING[c] for c in metadata_cols] if rename_fields else metadata_cols

        index = ["sj_div", "sj_nm", "account_nm"]
        index = [DEFAULT_RENAME_MAPPING[i] for i in index] if rename_fields else index
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, sort_by=sort_by, rename=rename, index=index
        )

    def get_xbrl_taxonomies(
        self, detailed_financial_statement_type: str, *, rename_fields: bool = True
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeFinancialInformationClient, self).get_xbrl_taxonomies(detailed_financial_statement_type)
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        return construct_dataframe(items, rename=rename)
