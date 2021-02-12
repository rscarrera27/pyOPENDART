from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

from pyopendart.clients.dict.base import DictClient
from pyopendart.enums import Market


@dataclass
class DateRange:
    begin: date  # bgn_de
    end: date  # end_de

    def serialize(self):
        return {"bgn_de": self.begin.strftime("%Y%m%d"), "end_de": self.end.strftime("%Y%m%d")}


class DisclosureType(Enum):
    A = "A"  # 정기공시
    B = "B"  # 주요사항보고
    C = "C"  # 발행공시
    D = "D"  # 지분공시
    E = "E"  # 기타공시
    F = "F"  # 외부감사관련
    G = "G"  # 펀드공시
    H = "H"  # 자산유동화
    I = "I"  # 거래소공시
    J = "J"  # 공정위공시


@dataclass
class Sort:
    class By(Enum):
        DATE = "date"
        CORP_NAME = "crp"
        REPORT_NAME = "rpt"

    by: By  # sort
    ascending: bool = False  # sort_mth

    def serialize(self) -> dict:
        return {"sort": self.by.value, "sort_mth": "asc" if self.ascending else "desc"}


class DisclosureClient(DictClient):
    def search(
        self,
        corporation_code: Optional[str] = None,  # corp_code
        date_range: Optional[DateRange] = None,  # bgn_de, end_de
        only_last_report: Optional[bool] = None,  # last_reprt_at
        type: Optional[DisclosureType] = None,  # pblntf_ty
        type_detail: Optional[str] = None,  # pblntf_detail_ty TODO: enum
        market: Optional[Market] = None,  # corp_cls
        sort: Optional[Sort] = None,  # sort, sort_mth
        page: int = 1,
        limit: int = 20,
    ) -> dict:
        params = {
            "corp_code": corporation_code if corporation_code else None,
            "last_reprt_at": {True: "Y", False: "N"}.get(only_last_report),
            "pblntf_ty": type.value if type else None,
            "pblntf_detail_ty": type_detail if type_detail else None,
            "corp_cls": market.value if market else None,
            "page_no": str(page),
            "page_count": str(limit),
        }
        params.update(date_range.serialize()) if date_range else None
        params.update(sort.serialize()) if sort else None
        params = {k: v for k, v in params.items() if v is not None}

        return self.client.json("list", **params)

    def get_company_overview(
        self,
        corporation_code: str,  # corp_code
    ) -> dict:
        return self.client.json("company", corp_code=corporation_code)
