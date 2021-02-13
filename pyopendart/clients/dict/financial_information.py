from typing import Sequence

from pyopendart.clients.base import ClientBase
from pyopendart.enums import FinancialStatementDivision, ReportType


class FinancialInformationClient(ClientBase):
    def get_financial_statements_of_major_accounts(
        self, corporation_codes: Sequence[str], business_year: int, report_type: ReportType
    ) -> Sequence[dict]:
        if len(corporation_codes) == 0:
            return []
        elif len(corporation_codes) == 1:
            params = {
                "corp_code": corporation_codes[0],
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            return self.client.json("fnlttSinglAcnt", params).get("list", [])

        else:
            params = {
                "corp_code": ','.join(corporation_codes),
                "bsns_year": str(business_year),
                "reprt_code": report_type.value,
            }
            return self.client.json("fnlttMultiAcnt", params).get("list", [])

    def get_full_financial_statements(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        financial_statement_division: FinancialStatementDivision = FinancialStatementDivision.FINANCIAL_STATEMENT,
    ) -> Sequence[dict]:
        params = {
            "corp_code": corporation_code,
            "bsns_year": str(business_year),
            "reprt_code": report_type.value,
            "fs_div": financial_statement_division.value,
        }
        return self.client.json("fnlttSinglAcntAll", params).get("list", [])

    def get_xbrl_taxonomies(self, detailed_financial_statement_type: str) -> Sequence[dict]:
        params = {"sj_div": detailed_financial_statement_type}
        return self.client.json("xbrlTaxonomy", params).get("list", [])
