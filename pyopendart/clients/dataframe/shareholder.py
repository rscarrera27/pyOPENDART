from typing import Optional, Tuple

import pandas as pd

from pyopendart.clients.dataframe.utils import DEFAULT_RENAME_MAPPING, construct_dataframe, get_converters
from pyopendart.clients.namedtuple.shareholder import NamedtupleShareholderReportClient


class DataframeShareholderReportClient(NamedtupleShareholderReportClient):
    def get_major_shareholder_reports(
        self, corporation_code: str, *, convert_data: bool = True, rename_fields: bool = True, set_index: bool = True
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeShareholderReportClient, self).get_major_shareholder_reports(corporation_code)

        converters = (
            get_converters(
                "stkqy",
                "stkqy_irds",
                "stkrt",
                "stkrt_irds",
                "ctr_stkqy",
                "ctr_stkrt",
            )
            if convert_data
            else None
        )
        sort_by = ["rcept_dt"]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        metadata_cols = ["corp_code", "corp_name"]
        metadata_cols = [DEFAULT_RENAME_MAPPING[c] for c in metadata_cols] if rename_fields else metadata_cols

        index = ["rcept_no", "rcept_dt", "repror"]
        index = [DEFAULT_RENAME_MAPPING[i] for i in index] if rename_fields else index
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, sort_by=sort_by, rename=rename, index=index
        )

    def get_executive_shareholder_reports(
        self, corporation_code: str, *, convert_data: bool = True, rename_fields: bool = True, set_index: bool = True
    ) -> Tuple[pd.DataFrame, Optional[dict]]:
        items = super(DataframeShareholderReportClient, self).get_executive_shareholder_reports(corporation_code)

        converters = (
            get_converters(
                "isu_exctv_rgist_at",
                "sp_stock_lmp_cnt",
                "sp_stock_lmp_irds_cnt",
                "sp_stock_lmp_rate",
                "sp_stock_lmp_irds_rate",
            )
            if convert_data
            else None
        )
        sort_by = ["rcept_dt"]
        rename = DEFAULT_RENAME_MAPPING if rename_fields else None

        metadata_cols = ["corp_code", "corp_name"]
        metadata_cols = [DEFAULT_RENAME_MAPPING[c] for c in metadata_cols] if rename_fields else metadata_cols

        index = ["rcept_no", "rcept_dt", "repror"]
        index = [DEFAULT_RENAME_MAPPING[i] for i in index] if rename_fields else index
        index = index if set_index else None

        return construct_dataframe(
            items, converters=converters, metadata_cols=metadata_cols, sort_by=sort_by, rename=rename, index=index
        )
