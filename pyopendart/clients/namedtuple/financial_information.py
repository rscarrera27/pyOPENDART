from collections import namedtuple
from typing import Sequence

from pyopendart.clients.dict.financial_information import FinancialInformationClient
from pyopendart.enums import FinancialStatementDivision, ReportType

MajorAccountItem = namedtuple(
    "MajorAccountItem",
    [
        'rcept_no',
        'reprt_code',
        'bsns_year',
        'corp_code',
        'stock_code',
        'fs_div',
        'fs_nm',
        'sj_div',
        'sj_nm',
        'account_nm',
        'thstrm_nm',
        'thstrm_dt',
        'thstrm_amount',
        'thstrm_add_amount',
        'frmtrm_nm',
        'frmtrm_dt',
        'frmtrm_amount',
        'frmtrm_add_amount',
        'bfefrmtrm_nm',
        'bfefrmtrm_dt',
        'bfefrmtrm_amount',
        'ord',
    ],
    defaults=[""] * 20,
)


FullFinancialStatementItem = namedtuple(
    "FullFinancialStatementItem",
    [
        'rcept_no',
        'reprt_code',
        'bsns_year',
        'corp_code',
        'sj_div',
        'sj_nm',
        'account_id',
        'account_nm',
        'account_detail',
        'thstrm_nm',
        'thstrm_amount',
        'thstrm_add_amount',
        'frmtrm_nm',
        'frmtrm_amount',
        'frmtrm_q_nm',
        'frmtrm_q_amount',
        'frmtrm_add_amount',
        'bfefrmtrm_nm',
        'bfefrmtrm_amount',
        'ord',
    ],
    defaults=[""] * 20,
)

XbrlTaxonomy = namedtuple(
    "XbrlTaxonomy",
    [
        'sj_div',
        'bsns_de',
        'account_id',
        'account_nm',
        'label_kor',
        'label_eng',
        'data_tp',
        'ifrs_ref',
    ],
    defaults=[""] * 8,
)


class NamedtupleFinancialInformationClient(FinancialInformationClient):
    def get_financial_statements_of_major_accounts(
        self, corporation_codes: Sequence[str], business_year: int, report_type: ReportType
    ) -> Sequence[MajorAccountItem]:
        items = super(NamedtupleFinancialInformationClient, self).get_financial_statements_of_major_accounts(
            corporation_codes, business_year, report_type
        )
        return [MajorAccountItem(**i) for i in items]

    def get_full_financial_statements(
        self,
        corporation_code: str,
        business_year: int,
        report_type: ReportType,
        financial_statement_division: FinancialStatementDivision = FinancialStatementDivision.FINANCIAL_STATEMENT,
    ) -> Sequence[FullFinancialStatementItem]:
        items = super(NamedtupleFinancialInformationClient, self).get_full_financial_statements(
            corporation_code,
            business_year,
            report_type,
            financial_statement_division,
        )
        return [FullFinancialStatementItem(**i) for i in items]

    def get_xbrl_taxonomies(self, detailed_financial_statement_type: str) -> Sequence[XbrlTaxonomy]:
        items = super(NamedtupleFinancialInformationClient, self).get_xbrl_taxonomies(detailed_financial_statement_type)
        return [XbrlTaxonomy(**i) for i in items]
