from typing import Sequence

from pyopendart.clients.base import ClientBase


class ShareholderReportClient(ClientBase):
    def get_major_shareholder_reports(self, corporation_code: str) -> Sequence[dict]:
        params = {"corp_code": corporation_code}
        return self.client.xml("majorstock", params).get("list", [])

    def get_executive_shareholder_reports(self, corporation_code: str) -> Sequence[dict]:
        params = {"corp_code": corporation_code}
        return self.client.xml("elestock", params).get("list", [])
