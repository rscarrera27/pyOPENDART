from datetime import datetime
from typing import Mapping, Optional, Set

import pandas as pd
from dateutil.parser import parse as datetime_parse

from pyopendart.api.const import ENG_TO_KOR_RENAME_MAPPING, KNOWN_DATE_FIELDS, KNOWN_NUMERIC_FIELDS, KNOWN_RATIO_FIELDS
from pyopendart.utils import dart_atoi, is_dart_null


def convert_known_numeric_fields(df: pd.DataFrame, *, known_fields: Set[str] = KNOWN_NUMERIC_FIELDS) -> pd.DataFrame:
    numeric_cols = [c for c in df.columns.values if c in known_fields]

    for c in numeric_cols:
        df[c] = df[c].apply(dart_atoi)

    return df


def convert_known_ratio_fields(df: pd.DataFrame, *, known_fields: Set[str] = KNOWN_RATIO_FIELDS) -> pd.DataFrame:
    ratio_cols = [c for c in df.columns.values if c in known_fields]

    for c in ratio_cols:
        df[c] = df[c].apply(lambda v: dart_atoi(v.replace("%", "")))

    return df


def convert_known_date_fields(df: pd.DataFrame, *, known_fields: Set[str] = KNOWN_DATE_FIELDS) -> pd.DataFrame:
    date_cols = [c for c in df.columns.values if c in known_fields]
    known_converters = {
        "%Y년 %m월 %d일": lambda v: datetime.strptime(v, "%Y년 %m월 %d일").date() if not is_dart_null(v) else "",
        "%Y%m%d": lambda v: datetime.strptime(v, "%Y%m%d").date() if not is_dart_null(v) else "",
        "": lambda v: datetime_parse(v).date() if not is_dart_null(v) else "",
    }

    for c in date_cols:
        series = df[c]

        for k, f in known_converters.items():
            try:
                series = df[c].apply(f)
                break
            except:
                continue

        df[c] = series

    return df


def rename_fields(
    df: pd.DataFrame, *, mapping: Optional[Mapping[str, str]] = ENG_TO_KOR_RENAME_MAPPING
) -> pd.DataFrame:
    if not mapping:
        return df

    df = df.rename(
        columns={k: mapping.get(k, k) for k in df.columns.values},
    )

    return df
