from collections import namedtuple
from datetime import date
from typing import List, Optional, Tuple

from pyopendart.clients.dict.disclosure import DateRange, DisclosureClient, Sort
from pyopendart.enums import DisclosureType, Market, SortBy

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


class NamedtupleDisclosureClient(DisclosureClient):
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
    ) -> Tuple[List[SearchResultItem], dict]:
        resp = super(NamedtupleDisclosureClient, self).search(
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
        items = [SearchResultItem(**i) for i in resp.pop("list")]

        return items, resp

    def get_company_overview(
        self,
        corporation_code: str,  # corp_code
    ) -> List[CompanyOverview]:
        resp = super(NamedtupleDisclosureClient, self).get_company_overview(corporation_code)
        return [CompanyOverview(**resp)]
