from pyopendart.clients.base import ClientBase
from pyopendart.enums import ReportType


class FinancialStatementFileDownloader(ClientBase):
    def get_xbrl_document(self, corporation_code: str, report_type: ReportType):
        params = {
            "corp_code": corporation_code,
            "reprt_code": report_type.value,
        }
        self.client.download("fnlttXbrl", params)
