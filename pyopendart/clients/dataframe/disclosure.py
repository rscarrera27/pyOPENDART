from typing import Optional, Tuple

import pandas as pd

from pyopendart.clients.dataframe.utils import DEFAULT_RENAME_MAPPING, construct_dataframe, get_converters
from pyopendart.clients.dict.disclosure import DateRange, DisclosureType, Sort
from pyopendart.clients.namedtuple.disclosure import NamedtupleDisclosureClient
from pyopendart.enums import Market


class DataframeDisclosureClient(NamedtupleDisclosureClient):
    def search(
        self,
        corporation_code: Optional[str] = None,
        date_range: Optional[DateRange] = None,
        only_last_report: Optional[bool] = None,
        type: Optional[DisclosureType] = None,
        type_detail: Optional[str] = None,
        market: Optional[Market] = None,
        sort: Optional[Sort] = None,
        page: int = 1,
        limit: int = 20,
        *,
        convert_data: bool = True,
        rename_fields: bool = True,
        set_index: bool = True,
    ) -> Tuple[pd.DataFrame, Optional[dict], dict]:
        items, pagination = super(DataframeDisclosureClient, self).search(
            corporation_code, date_range, only_last_report, type, type_detail, market, sort, page, limit
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
        converters = get_converters("jurir_no", "bizr_no", "induty_code", "est_dt", "acc_mt") if convert_data else None
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        return construct_dataframe(items, converters=converters, rename=rename)


if __name__ == "__main__":
    from datetime import date, datetime

    c = DataframeDisclosureClient("e32e1ae12ac94446f3133bc0b7e42491b0cde4a3")

    r1 = c.search(
        date_range=DateRange(begin=date(year=2021, month=1, day=1), end=datetime.now().date()),
        market=Market.KOSPI,
    )
    r2 = c.get_company_overview("00126380")

    print(r1)
