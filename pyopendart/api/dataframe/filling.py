from datetime import date
from typing import Optional, Tuple, Union

import pandas as pd

from pyopendart.api.base import ApiBase
from pyopendart.api.const import RENAME_MAPPINGS
from pyopendart.api.dataframe.utils import (
    convert_known_date_fields,
    convert_known_numeric_fields,
    convert_known_ratio_fields,
    rename_fields,
)
from pyopendart.enums import DisclosureType, DisclosureTypeDetail, Market, RenameMode, SortBy
from pyopendart.utils import dart_atoi


class FillingApi(ApiBase):
    def search(
        self,
        corporation_code: Optional[str] = None,
        date_begin: Optional[date] = None,
        date_end: Optional[date] = None,
        only_last_report: Optional[bool] = None,
        type: Optional[Union[DisclosureType, str]] = None,
        type_detail: Optional[Union[DisclosureTypeDetail, str]] = None,
        market: Optional[Market] = None,
        sort_by: Optional[SortBy] = None,
        ascending: bool = False,
        page: int = 1,
        limit: int = 20,
        *,
        rename: Optional[RenameMode] = RenameMode.ENG,
    ) -> Tuple[pd.DataFrame, dict]:
        params = {
            "corp_code": corporation_code if corporation_code else None,
            "bgn_de": date_begin.strftime("%Y%m%d") if date_begin else None,
            "end_de": date_end.strftime("%Y%m%d") if date_end else None,
            "last_reprt_at": {True: "Y", False: "N"}.get(only_last_report),
            "pblntf_ty": str(type) if type else None,
            "pblntf_detail_ty": str(type_detail) if type_detail else None,
            "corp_cls": market.value if market else None,
            "sort_by": sort_by.value if sort_by else None,
            "ascending": ("asc" if ascending else "desc") if ascending else None,
            "page_no": str(page),
            "page_count": str(limit),
        }
        params = {k: v for k, v in params.items() if v is not None}
        search_res = self.client.xml_resource("list", params)

        pagination = {
            "page": dart_atoi(search_res.find("page_no").text),
            "total_page": dart_atoi(search_res.find("total_page").text),
            "page_count": dart_atoi(search_res.find("page_count").text),
            "total_count": dart_atoi(search_res.find("total_count").text),
        }

        df = pd.DataFrame({element.tag: element.text for element in item} for item in search_res.iter("list"))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df, pagination

    def get_company_overview(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> pd.DataFrame:
        res = self.client.json_resource("company", {'corp_code': corporation_code})

        df = pd.DataFrame([res])
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df

    def get_filling_file(self, receipt_no: str, save_to: str):
        self.client.zip_resource("document", {"rcept_no": receipt_no}, save_to=save_to)

    def get_corporation_codes(self, save_to: str):
        self.client.zip_resource("corpCode", {}, save_to=save_to)
