from datetime import date
from typing import Optional, Sequence, Tuple, Union

from pyopendart.api.dataframe.filling import FillingApi as DfFillingApi
from pyopendart.enums import DisclosureType, DisclosureTypeDetail, Market, RenameMode, SortBy


class FillingApi(DfFillingApi):
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
    ) -> Tuple[Sequence[dict], dict]:
        df, pagination = super(FillingApi, self).search(
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
            rename=rename,
        )
        items = df.to_dict("records")

        return items, pagination

    def get_company_overview(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> Sequence[dict]:
        df = super(FillingApi, self).get_company_overview(corporation_code, rename=rename)

        return df.to_dict("records")

    def get_filling_file(self, receipt_no: str, save_to: str):
        self.client.zip_resource("document", {"rcept_no": receipt_no}, save_to=save_to)

    def get_corporation_codes(self, save_to: str):
        self.client.zip_resource("corpCode", {}, save_to=save_to)
