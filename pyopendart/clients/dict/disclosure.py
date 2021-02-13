from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional

from pyopendart.clients.base import ClientBase
from pyopendart.enums import DisclosureType, Market, SortBy


@dataclass
class DateRange:
    begin: date  # bgn_de
    end: date  # end_de

    def serialize(self):
        return {"bgn_de": self.begin.strftime("%Y%m%d"), "end_de": self.end.strftime("%Y%m%d")}


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


class DisclosureClient(ClientBase):
    def search(
        self,
        corporation_code: Optional[str] = None,  # corp_code
        date_begin: Optional[date] = None,  # bgn_de
        date_end: Optional[date] = None,  # end_de
        only_last_report: Optional[bool] = None,  # last_reprt_at
        type: Optional[DisclosureType] = None,  # pblntf_ty
        type_detail: Optional[str] = None,  # pblntf_detail_ty TODO: enum
        market: Optional[Market] = None,  # corp_cls
        sort_by: Optional[SortBy] = None,
        ascending: bool = False,
        page: int = 1,
        limit: int = 20,
    ) -> dict:
        params = {
            "corp_code": corporation_code if corporation_code else None,
            "bgn_de": date_begin.strftime("%Y%m%d") if date_begin else None,
            "end_de": date_end.strftime("%Y%m%d") if date_end else None,
            "last_reprt_at": {True: "Y", False: "N"}.get(only_last_report),
            "pblntf_ty": type.value if type else None,
            "pblntf_detail_ty": type_detail if type_detail else None,
            "corp_cls": market.value if market else None,
            "sort_by": sort_by.value if sort_by else None,
            "ascending": ("asc" if ascending else "desc") if ascending else None,
            "page_no": str(page),
            "page_count": str(limit),
        }
        params = {k: v for k, v in params.items() if v is not None}

        return self.client.json("list", params)

    def get_company_overview(
        self,
        corporation_code: str,  # corp_code
    ) -> dict:
        return self.client.json("company", {'corp_code': corporation_code})
