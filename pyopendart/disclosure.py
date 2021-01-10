from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional, Tuple

from pyopendart.common import DartClient


@dataclass
class DateRange:
    begin: date  # bgn_de
    end: date  # end_de

    def serialize(self):
        return {"bgn_de": self.begin.strftime("%Y%m%d"), "end_de": self.end.strftime("%Y%m%d")}


class PublicNotificationType(Enum):
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


class Market(Enum):
    KOSPI = "Y"
    KOSDAQ = "K"
    KONEX = "N"
    ETC = "E"

    def __missing__(self, key):
        return None


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


@dataclass(frozen=True)
class SearchResult:
    current_page: Pagination
    total_page: int
    total_count: int

    @dataclass(frozen=True)
    class ResultItem:
        corporation_code: str
        corporation_name: str
        stock_code: str
        market: Market
        report_name: str
        receipt_no: str
        filler_name: str
        receipt_date: str
        remarks: str

        @staticmethod
        def from_dart_resp(resp):
            return SearchResult.ResultItem(
                corporation_code=resp.get("corp_code"),
                corporation_name=resp.get("corp_name"),
                stock_code=resp.get("stock_code"),
                market=Market(resp.get("corp_cls")),
                report_name=resp.get("report_nm"),
                receipt_no=resp.get("rcept_no"),
                filler_name=resp.get("flr_nm"),
                receipt_date=resp.get("rcept_dt"),
                remarks=resp.get("rm"),
            )

    items: Tuple[ResultItem]

    @staticmethod
    def from_dart_resp(resp: dict) -> "SearchResult":

        return SearchResult(
            current_page=Pagination(page_no=resp.get("page_no"), items_per_page=resp.get("page_count")),
            total_page=resp.get("total_page"),
            total_count=resp.get("total_count"),
            items=tuple(SearchResult.ResultItem.from_dart_resp(i) for i in resp.get("list", [])),
        )


@dataclass(frozen=True)
class CompanyOverview:
    @dataclass(frozen=True)
    class Name:
        kor: str
        eng: str
        stock: str

    name: Name  # corp_name, corp_name_eng, stock_name
    ticker: str  # stock_code
    ceo_name: str  # ceo_nm
    market: Market  # corp_cls
    corporation_registration_number: str  # jurir_no
    business_registration_number: str  # bizr_no
    address: str  # adres
    homepage_url: str  # hm_url
    ir_url: str  # ir_url
    phone_number: str  # phn_no
    fax_number: str  # fax_no
    industry_code: str  # induty_code
    established_date: date  # est_dt
    accounting_month: int  # acc_mt

    @staticmethod
    def from_dart_resp(resp):
        return CompanyOverview(
            name=CompanyOverview.Name(
                kor=resp.get("corp_name"),
                eng=resp.get("corp_name_eng"),
                stock=resp.get("stock_name"),
            ),
            ticker=resp.get("stock_code"),
            ceo_name=resp.get("ceo_nm"),
            market=Market(resp.get("corp_cls")),
            corporation_registration_number=resp.get("jurir_no"),
            business_registration_number=resp.get("bizr_no"),
            address=resp.get("adres"),
            homepage_url=resp.get("hm_url"),
            ir_url=resp.get("ir_url"),
            phone_number=resp.get("phn_no"),
            fax_number=resp.get("fax_no"),
            industry_code=resp.get("induty_code"),
            established_date=resp.get("est_dt"),
            accounting_month=resp.get("acc_mt"),
        )


class PublicNotification:
    def __init__(self, api_key: str) -> None:
        self.client = DartClient(api_key)

    def search(
        self,
        corporation_code: Optional[str] = None,  # corp_code
        date_range: Optional[DateRange] = None,  # bgn_de, end_de
        only_last_report: Optional[bool] = None,  # last_reprt_at
        type: Optional[PublicNotificationType] = None,  # pblntf_ty
        type_detail: Optional[str] = None,  # pblntf_detail_ty TODO: enum
        market: Optional[Market] = None,  # corp_cls
        sort: Optional[Sort] = None,  # sort, sort_mth
        pagination: Optional[Pagination] = None,
    ) -> SearchResult:
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

        return SearchResult.from_dart_resp(resp)

    def company_overview(
        self,
        corporation_code: str,  # corp_code
    ) -> CompanyOverview:
        resp = self.client.json("company", corp_code=corporation_code)
        return CompanyOverview.from_dart_resp(resp)
