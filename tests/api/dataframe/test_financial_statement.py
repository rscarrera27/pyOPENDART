import pytest

from pyopendart.api.const import ENG_TO_ENG_RENAME_MAPPING, ENG_TO_KOR_RENAME_MAPPING
from pyopendart.api.dataframe.financial_statement import FinancialStatementApi
from pyopendart.enums import FinancialStatementDivision, FinancialStatementTypeDetail, RenameMode, ReportType
from tests.config import TEST_CLIENT_KEY


@pytest.mark.parametrize(
    "corp_codes",
    [["00293886", "00126380"], ["00356361"]],
)
def test_get_financial_statements_of_major_accounts(corp_codes):
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_financial_statements_of_major_accounts(corp_codes, 2019, ReportType.ANNUAL)

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


@pytest.mark.parametrize(
    "corp_codes",
    [["00293886", "00126380"], ["00356361"]],
)
def test_get_financial_statements_of_major_accounts_kor_rename(corp_codes):
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_financial_statements_of_major_accounts(corp_codes, 2019, ReportType.ANNUAL, rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()


def test_get_full_financial_statements():
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_full_financial_statements(
        "00126380", 2019, ReportType.ANNUAL, FinancialStatementDivision.CONSOLIDATED_FINANCIAL_STATEMENT
    )

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_get_full_financial_statements_kor_rename():
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_full_financial_statements(
        "00126380",
        2019,
        ReportType.ANNUAL,
        FinancialStatementDivision.CONSOLIDATED_FINANCIAL_STATEMENT,
        rename=RenameMode.KOR,
    )

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()


def test_get_xbrl_taxonomies():
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_xbrl_taxonomies(FinancialStatementTypeDetail.BS1)

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_get_xbrl_taxonomies_kor_rename():
    api = FinancialStatementApi(TEST_CLIENT_KEY)
    df = api.get_xbrl_taxonomies(FinancialStatementTypeDetail.BS1, rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()
