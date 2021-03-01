from pyopendart.api.const import ENG_TO_ENG_RENAME_MAPPING, ENG_TO_KOR_RENAME_MAPPING
from pyopendart.api.dataframe.shareholders_report import ShareholdersReportApi
from pyopendart.enums import RenameMode
from tests.config import TEST_CLIENT_KEY


def test_get_major_shareholder_reports():
    api = ShareholdersReportApi(TEST_CLIENT_KEY)
    df = api.get_major_shareholder_reports("00126380")

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_get_major_shareholder_reports_kor_rename():
    api = ShareholdersReportApi(TEST_CLIENT_KEY)
    df = api.get_major_shareholder_reports("00126380", rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()


def test_get_executive_shareholder_reports():
    api = ShareholdersReportApi(TEST_CLIENT_KEY)
    df = api.get_executive_shareholder_reports("00126380")

    for k in df.columns.values:
        assert k in ENG_TO_ENG_RENAME_MAPPING.values(), df.to_string()


def test_get_executive_shareholder_reports_kor_rename():
    api = ShareholdersReportApi(TEST_CLIENT_KEY)
    df = api.get_executive_shareholder_reports("00126380", rename=RenameMode.KOR)

    for k in df.columns.values:
        assert k in ENG_TO_KOR_RENAME_MAPPING.values(), df.to_string()
