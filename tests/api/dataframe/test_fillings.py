from datetime import date

from pyopendart.api.const import ENG_TO_ENG_RENAME_MAPPING, ENG_TO_KOR_RENAME_MAPPING
from pyopendart.api.dataframe.filling import FillingApi
from pyopendart.enums import Market, RenameMode
from tests.config import TEST_CLIENT_KEY


def test_search_with():
    api = FillingApi(TEST_CLIENT_KEY)
    df, pagination = api.search(
        date_begin=date(year=2021, month=1, day=1),
        date_end=date(year=2021, month=2, day=1),
        market=Market.KOSPI,
    )

    assert isinstance(pagination, dict)
    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_search_with_kor_rename():
    api = FillingApi(TEST_CLIENT_KEY)
    df, pagination = api.search(
        date_begin=date(year=2021, month=1, day=1),
        date_end=date(year=2021, month=2, day=1),
        market=Market.KOSPI,
        rename=RenameMode.KOR,
    )

    assert isinstance(pagination, dict)
    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()


def test_get_company_overview():
    api = FillingApi(TEST_CLIENT_KEY)
    df = api.get_company_overview("00126380")

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_get_company_overview_kor_rename():
    api = FillingApi(TEST_CLIENT_KEY)
    df = api.get_company_overview("00126380", rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()
