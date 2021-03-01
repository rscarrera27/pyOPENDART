from typing import Optional, Union

from numpy import NaN


def is_dart_null(v: Optional[str]) -> bool:
    _know_dart_null = ("-", "\u3000-", "")

    if v is None:
        return True

    if v in _know_dart_null:
        return True

    return False


def dart_atoi(a: str) -> Optional[Union[int, float]]:
    try:
        try:
            return int(a.replace(",", ""))
        except ValueError as e:
            return float(a.replace(",", ""))
    except (ValueError, AttributeError):
        return NaN
