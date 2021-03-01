from typing import Optional, Sequence, Union

from pyopendart.api.dataframe.financial_statement import FinancialStatementApi as DfFinancialStatementApi
from pyopendart.enums import FinancialStatementDivision, FinancialStatementTypeDetail, RenameMode, ReportType


class FinancialStatementApi(DfFinancialStatementApi):
    def get_financial_statements_of_major_accounts(
        self,
        corporation_codes: Sequence[str],
        business_year: int,
        report_type: ReportType,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(FinancialStatementApi, self).get_financial_statements_of_major_accounts(
            corporation_codes, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

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
    ) -> Sequence[dict]:
        df = super(FinancialStatementApi, self).get_full_financial_statements(
            corporation_code, business_year, report_type, rename=rename
        )
        return df.to_dict("records")

    def get_xbrl_taxonomies(
        self,
        detailed_financial_statement_type: Union[FinancialStatementTypeDetail, str],
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Sequence[dict]:
        df = super(FinancialStatementApi, self).get_xbrl_taxonomies(detailed_financial_statement_type, rename=rename)
        return df.to_dict("records")
