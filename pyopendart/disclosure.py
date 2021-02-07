from collections import namedtuple
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional, Tuple

import pandas as pd
from dateutil.parser import parse as datetime_parse

from pyopendart.client import DartClient
from pyopendart.common import DateRange, DisclosureType, Market


class SortBy(Enum):
    DATE = "date"
    CORP_NAME = "crp"
    REPORT_NAME = "rpt"


@dataclass
class Sort:
    sort_by: SortBy  # sort
    sort_desc: bool = True  # sort_mth

    def serialize(self) -> dict:
        return {"sort": self.sort_by.value, "sort_mth": "desc" if self.sort_desc else "asc"}


@dataclass
class Pagination:
    page_no: int  # page_no
    items_per_page: int  # page_count

    def serialize(self) -> dict:
        return {"page_no": str(self.page_no), "page_count": str(self.items_per_page)}


SearchResultItem = namedtuple(
    "SearchResultItem",
    ["corp_code", "corp_name", "stock_code", "corp_cls", "report_nm", "rcept_no", "flr_nm", "rcept_dt", "rm"],
)

CompanyOverview = namedtuple(
    "CompanyOverview",
    [
        'corp_code',
        'corp_name',
        'corp_name_eng',
        'stock_name',
        'stock_code',
        'ceo_nm',
        'corp_cls',
        'jurir_no',
        'bizr_no',
        'adres',
        'hm_url',
        'ir_url',
        'phn_no',
        'fax_no',
        'induty_code',
        'est_dt',
        'acc_mt',
    ],
)


class Disclosure:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def search(
        self,
        corporation_code: Optional[str] = None,  # corp_code
        date_range: Optional[DateRange] = None,  # bgn_de, end_de
        only_last_report: Optional[bool] = None,  # last_reprt_at
        type: Optional[DisclosureType] = None,  # pblntf_ty
        type_detail: Optional[str] = None,  # pblntf_detail_ty TODO: enum
        market: Optional[Market] = None,  # corp_cls
        sort: Optional[Sort] = None,  # sort, sort_mth
        pagination: Optional[Pagination] = None,
    ) -> Tuple[dict, pd.DataFrame]:
        params = {
            "corp_code": corporation_code if corporation_code else None,
            "last_reprt_at": {True: "Y", False: "N"}.get(only_last_report),
            "pblntf_ty": type.value if type else None,
            "pblntf_detail_ty": type_detail if type_detail else None,
            "corp_cls": market.value if market else None,
        }
        params.update(date_range.serialize()) if date_range else None
        params.update(sort.serialize()) if sort else None
        params.update(pagination.serialize()) if pagination else None
        params = {k: v for k, v in params.items() if v is not None}

        resp = self.client.json("list", **params)

        items = [SearchResultItem(**i) for i in resp.pop("list")]

        df = pd.DataFrame(items)
        df["rcept_dt"] = df["rcept_dt"].apply(lambda v: datetime_parse(v).date())
        df["corp_cls"] = df["corp_cls"].apply(Market)
        df = df.rename(
            columns={
                "corp_code": "corporation_code",
                "corp_name": "corporation_name",
                "stock_code": "stock_code",
                "corp_cls": "market",
                "report_nm": "report_name",
                "rcept_no": "receipt_no",
                "flr_nm": "filler_name",
                "rcept_dt": "receipt_date",
                "rm": "remarks",
            }
        )

        return resp, df

    def get_company_overview(
        self,
        corporation_code: str,  # corp_code
    ) -> pd.DataFrame:
        resp = self.client.json("company", corp_code=corporation_code)

        df = pd.DataFrame([CompanyOverview(**resp)])
        df["est_dt"] = df["est_dt"].apply(lambda v: datetime_parse(v).date())
        df["corp_cls"] = df["corp_cls"].apply(Market)
        df = df.rename(
            columns={
                "corp_code": "corporation_code",
                "corp_name": "corporation_name",
                "stock_code": "stock_code",
                "stock_name": "stock_name",
                "ceo_nm": "ceo_name",
                "corp_cls": "market",
                "jurir_no": "corporation_registration_number",
                "bizr_no": "business_registration_number",
                "adres": "address",
                "hm_url": "homepage_url",
                "ir_url": "ir_url",
                "phn_no": "phone_number",
                "fax_no": "fax_number",
                "induty_code": "industry_code",
                "est_dt": "established_date",
                "acc_mt": "accounting_month",
            }
        )

        return df


