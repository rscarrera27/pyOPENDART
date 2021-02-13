from datetime import date
from typing import Optional, Tuple

import pandas as pd

from pyopendart.clients.dataframe.utils import DEFAULT_RENAME_MAPPING, construct_dataframe, get_converters
from pyopendart.clients.dict.disclosure import DateRange, Sort
from pyopendart.clients.namedtuple.disclosure import NamedtupleDisclosureClient
from pyopendart.enums import DisclosureType, Market, SortBy


class DataframeDisclosureClient(NamedtupleDisclosureClient):
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
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict], dict]:
        items, pagination = super(DataframeDisclosureClient, self).search(
            corporation_code,
            date_begin,
            date_end,
            only_last_report,
            type,
            type_detail,
            market,
            sort_by,
            ascending,
            page,
            limit,
        )
        converters = get_converters("corp_cls", "rcept_dt") if convert_data else None
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None
        df, meta = construct_dataframe(items, converters=converters, rename=rename)

        return df, meta, pagination

    def get_company_overview(
        self,
        corporation_code: str,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeDisclosureClient, self).get_company_overview(corporation_code)
        converters = (
            get_converters("corp_cls", "jurir_no", "bizr_no", "induty_code", "est_dt", "acc_mt")
            if convert_data
            else None
        )
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        return construct_dataframe(items, converters=converters, rename=rename)
