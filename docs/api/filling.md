# 공시정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.api.dataframe import FillingApi
    from pyopendart.enums import DisclosureType, DisclosureTypeDetail, Market, SortBy
    ```

=== "Dict"
    
    ```python
    from pyopendart.api.dict import FillingApi
    from pyopendart.enums import DisclosureType, DisclosureTypeDetail, Market, SortBy
    ```

## 공시검색

### Parameter

| Name             | Type                                         | DART Name        |
| ---------------- | -------------------------------------------- | ---------------- |
| corporation_code | `Optional[str]`                              | corp_code        |
| date_begin       | `Optional[date]`                             | bgn_de           |
| date_end         | `Optional[date]`                             | end_de           |
| only_last_report | `Optional[bool]`                             | last_reprt_at    |
| type             | `Optional[Union[DisclosureType, str]]`       | pblntf_ty        |
| type_detail      | `Optional[Union[DisclosureTypeDetail, str]]` | pblntf_detail_ty |
| market           | `Optional[Market]`                           | corp_cls         |
| sort             | `Optional[Sort]`                             | sort, sort_mth   |
| sort_by          | `Optional[SortBy]`                           | sort             |
| ascending        | `bool` (default False)                       | sort_mth         |
| page             | `int` (default 1)                            | page_no          |
| limit            | `int` (default 20)                           | page_count       |

### Usage

=== "Dataframe"

    ```python
    client = FillingApi("YOUR API KEY")

    df, pagination = client.search(
        date_begin=date(year=2021, month=1, day=1), date_end=datetime.now().date(),
        market=Market.KOSPI,
    )
    ```

=== "Dict"
    
    ```python
    client = FillingApi("YOUR API KEY")

    search_results, pagination = client.search(
        date_begin=date(year=2021, month=1, day=1), date_end=datetime.now().date(),
        market=Market.KOSPI,
    )
    ```
## 기업개황

### Parameter

| Name             | Type  | DART Name |
| ---------------- | ----- | --------- |
| corporation_code | `str` | corp_code |

### Usage

=== "Dataframe"

    ```python
    client = FillingApi("YOUR API KEY")

    df = client.get_company_overview("00126380")
    ```

=== "Dict"
    
    ```python
    client = FillingApi("YOUR API KEY")

    company_overview = client.get_company_overview("00126380")
    ```

## 공시서류원본파일(XML) 다운로드

ZIP 형태의 공시서류 원본파일 응답을 자동으로 압축 해제해 지정한 경로에 저장합니다.

### Parameter

| Name       | Type  | DART Name |
| ---------- | ----- | --------- |
| receipt_no | `str` | rcept_no  |

### Usage

```python
client = FillingApi("YOUR API KEY")

client.get_filling_file("20190401004781", "./temp")
```

## 공시대상회사 고유번호 목록 다운로드

ZIP 형태의 공시대상회사 고유번호 목록 응답을 자동으로 압축 해제해 지정한 경로에 저장합니다.

### Parameter

No parameter required.

### Usage

```python
client = FillingApi("YOUR API KEY")

client.get_corporation_codes("./temp")
```