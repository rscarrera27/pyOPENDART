from collections import namedtuple
from typing import Sequence

from pyopendart.clients.dict.shareholder import ShareholderReportClient

MajorShareholderReport = namedtuple(
    "MajorShareholder",
    [
        "rcept_no",
        "rcept_dt",
        "corp_code",
        "corp_name",
        "repror",
        "report_tp",
        "stkqy",
        "stkqy_irds",
        "stkrt",
        "stkrt_irds",
        "ctr_stkqy",
        "ctr_stkrt",
        "report_resn",
    ],
)

ExecutiveShareholderReport = namedtuple(
    "ExecutiveShareholder",
    [
        "rcept_no",
        "rcept_dt",
        "corp_code",
        "corp_name",
        "repror",
        "isu_exctv_rgist_at",
        "isu_exctv_ofcps",
        "isu_main_shrholdr",
        "sp_stock_lmp_cnt",
        "sp_stock_lmp_irds_cnt",
        "sp_stock_lmp_rate",
        "sp_stock_lmp_irds_rate",
    ],
)


class NamedtupleShareholderReportClient(ShareholderReportClient):
    def get_major_shareholder_reports(self, corporation_code: str) -> Sequence[MajorShareholderReport]:
        items = super(NamedtupleShareholderReportClient, self).get_major_shareholder_reports(corporation_code)
        return [MajorShareholderReport(**i) for i in items]

    def get_executive_shareholder_reports(self, corporation_code: str) -> Sequence[ExecutiveShareholderReport]:
        items = super(NamedtupleShareholderReportClient, self).get_executive_shareholder_reports(corporation_code)
        return [ExecutiveShareholderReport(**i) for i in items]
