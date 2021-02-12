from collections import namedtuple
from typing import Sequence

from pyopendart.clients.dict.shareholder import ShareholderClient

MajorShareholder = namedtuple(
    "MajorShareholder",
    [
        "rcept_no",
        "rcept_dt",
        "corp_code",
        "corp_name",
        "report_tp",
        "repror",
        "stkqy",
        "stkqy_irds",
        "stkrt",
        "stkrt_irds",
        "ctr_stkqy",
        "ctr_stkrt",
        "report_resn",
    ],
)

ExecutiveShareholder = namedtuple(
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


class NamedtupleShareholderClient(ShareholderClient):
    def get_major_shareholders(self, corporation_code: str) -> Sequence[MajorShareholder]:
        items = super(NamedtupleShareholderClient, self).get_major_shareholders(corporation_code)
        return [MajorShareholder(**i) for i in items]

    def get_executive_shareholders(self, corporation_code: str) -> Sequence[ExecutiveShareholder]:
        items = super(NamedtupleShareholderClient, self).get_executive_shareholders(corporation_code)
        return [ExecutiveShareholder(**i) for i in items]
