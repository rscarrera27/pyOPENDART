from typing import Optional, Sequence, Union

import pandas as pd

from pyopendart.api.base import ApiBase
from pyopendart.api.const import RENAME_MAPPINGS
from pyopendart.api.dataframe.utils import (
    convert_known_date_fields,
    convert_known_numeric_fields,
    convert_known_ratio_fields,
    rename_fields,
)
from pyopendart.enums import FinancialStatementDivision, FinancialStatementTypeDetail, RenameMode, ReportType


class FinancialStatementApi(ApiBase):
    def get_financial_statements_of_major_accounts(
        self,
        corporation_codes: Sequence[str],
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        if len(corporation_codes) > 1:
            params = {
                "corp_code": ','.join(corporation_codes),
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            df = pd.DataFrame(i for i in self.client.iter_list_resource("fnlttMultiAcnt", params))
        else:
            params = {
                "corp_code": corporation_codes[0],
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            df = pd.DataFrame(i for i in self.client.iter_list_resource("fnlttSinglAcnt", params))

        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df

    def get_xbrl_document(self, corporation_code: str, report_type: ReportType, save_to: str):
        params = {
            "corp_code": corporation_code,
            "reprt_code": report_type.value,
        }
        self.client.zip_resource("fnlttXbrl", params, save_to=save_to)

    def get_full_financial_statements(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        financial_statement_division: Union[
            FinancialStatementDivision, str
        ] = FinancialStatementDivision.FINANCIAL_STATEMENT,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        fs_div = (
            financial_statement_division.value
            if isinstance(financial_statement_division, FinancialStatementDivision)
            else financial_statement_division
        )
        params = {
            "corp_code": corporation_code,
            "bsns_year": str(business_year),
            "reprt_code": report_type.value,
            "fs_div": fs_div,
        }

        df = pd.DataFrame(i for i in self.client.iter_list_resource("fnlttSinglAcntAll", params))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df

    def get_xbrl_taxonomies(
        self,
        detailed_financial_statement_type: Union[FinancialStatementTypeDetail, str],
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> pd.DataFrame:
        params = {"sj_div": str(detailed_financial_statement_type)}

        df = pd.DataFrame(i for i in self.client.iter_list_resource("xbrlTaxonomy", params))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df
