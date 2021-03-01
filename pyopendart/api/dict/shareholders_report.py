from typing import Optional, Sequence

from pyopendart.api.dataframe.shareholders_report import ShareholdersReportApi as DfShareholdersReportApi
from pyopendart.enums import RenameMode


class ShareholdersReportApi(DfShareholdersReportApi):
    def get_major_shareholder_reports(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> Sequence[dict]:
        df = super(ShareholdersReportApi, self).get_major_shareholder_reports(corporation_code, rename=rename)
        return df.to_dict("records")

    def get_executive_shareholder_reports(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> Sequence[dict]:
        df = super(ShareholdersReportApi, self).get_executive_shareholder_reports(corporation_code, rename=rename)
        return df.to_dict("records")
