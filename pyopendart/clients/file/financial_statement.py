from pyopendart.clients.base import ClientBase
from pyopendart.enums import ReportType


class FinancialStatementFileDownloader(ClientBase):
    def get_xbrl_document(self, corporation_code: str, report_type: ReportType, save_to: str):
        params = {
            "corp_code": corporation_code,
            "reprt_code": report_type.value,
        }
        self.client.download("fnlttXbrl", params, save_to=save_to)
