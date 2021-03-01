from typing import Optional

import pandas as pd

from pyopendart.api.base import ApiBase
from pyopendart.api.const import RENAME_MAPPINGS
from pyopendart.api.dataframe.utils import (
    convert_known_date_fields,
    convert_known_numeric_fields,
    convert_known_ratio_fields,
    rename_fields,
)
from pyopendart.enums import RenameMode


class ShareholdersReportApi(ApiBase):
    def get_major_shareholder_reports(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> pd.DataFrame:
        params = {"corp_code": corporation_code}

        df = pd.DataFrame(i for i in self.client.iter_list_resource("majorstock", params))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df

    def get_executive_shareholder_reports(
        self, corporation_code: str, *, rename: Optional[RenameMode] = RenameMode.ENG
    ) -> pd.DataFrame:
        params = {"corp_code": corporation_code}

        df = pd.DataFrame(i for i in self.client.iter_list_resource("elestock", params))
        df = convert_known_numeric_fields(df)
        df = convert_known_ratio_fields(df)
        df = convert_known_date_fields(df)
        df = rename_fields(df, mapping=RENAME_MAPPINGS.get(rename))

        return df
