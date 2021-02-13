# 원본파일 다운로드

!!! note
    다운로드 타임아웃은 기본 타임아웃과 별개의 `default_download_timeout` 파라미터로 관리됩니다.

## 공시서류원본파일(XML) 다운로드

ZIP 형태의 공시서류 원본파일 응답을 자동으로 압축을 해제헤 지정한 경로에 저장합니다.

```python
from pyopendart.clients import DisclosureFileDownloader

client = (
    DisclosureFileDownloader("YOUR API KEY", default_download_timeout=30)
    .get_document("20190401004781", "./temp")
)

```

## 재무제표 원본파일(XBRL) 다운로드

재무제표 원본파일 (XBRL) 응답을 자동으로 압축 해제에 지정한 경로에 저장합니다.

```python
from pyopendart.clients import FinancialStatementFileDownloader
from pyopendart.enums import ReportType

client = (
    FinancialStatementFileDownloader("YOUR API KEY", default_download_timeout=30)
    .get_xbrl_document("20190401004781", ReportType.ANNUAL,  "./temp")
)

```