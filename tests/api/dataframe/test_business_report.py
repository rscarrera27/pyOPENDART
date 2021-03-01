import pytest

from pyopendart.api.const import ENG_TO_ENG_RENAME_MAPPING, ENG_TO_KOR_RENAME_MAPPING
from pyopendart.api.dataframe.business_report import BusinessReportApi
from pyopendart.enums import RenameMode, ReportType
from tests.config import TEST_CLIENT_KEY

BUSINESS_REPORT_API_METHODS = [
    'get_changes_in_equity',
    'get_changes_in_major_shareholder',
    'get_dividend_info',
    'get_employment_status',
    'get_executive_compensation_status',
    'get_executives',
    'get_individual_executive_compensation_status',
    'get_investment_in_other_corporations',
    'get_major_shareholders',
    'get_minority_shareholders_status',
    'get_top_5_individual_executive_compensation',
    'get_treasury_shares_status',
]

PARAMS = [
    {'corporation_code': "00293886", 'business_year': 2018, 'report_type': ReportType.ANNUAL},
    {'corporation_code': "00356361", 'business_year': 2018, 'report_type': ReportType.ANNUAL},
    {'corporation_code': "00126380", 'business_year': 2018, 'report_type': ReportType.ANNUAL},
]


@pytest.mark.parametrize("method", BUSINESS_REPORT_API_METHODS)
@pytest.mark.parametrize("params", PARAMS)
def test_business_report_api(method, params):
    api = BusinessReportApi(TEST_CLIENT_KEY)
    df = getattr(api, method)(**params)

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


@pytest.mark.parametrize("method", BUSINESS_REPORT_API_METHODS)
@pytest.mark.parametrize("params", PARAMS)
def test_business_report_api_kor_rename(method, params):
    api = BusinessReportApi(TEST_CLIENT_KEY)
    df = getattr(api, method)(**params, rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()
