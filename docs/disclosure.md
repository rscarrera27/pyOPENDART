# 공시정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.clients.dataframe.disclosure import DataframeDisclosureClient
    from pyopendart.clients.dict.disclosure import DateRange
    from pyopendart.enums import Market
    ```

=== "Namedtuple"
    
    ```python
    from pyopendart.clients.namedtuple.disclosure import NamedtupleDisclosureClient
    from pyopendart.clients.dict.disclosure import DateRange
    from pyopendart.enums import Market
    ```

=== "Dict"
    
    ```python
    from pyopendart.clients.dict.disclosure import DisclosureClient
    from pyopendart.clients.dict.disclosure import DateRange
    from pyopendart.enums import Market
    ```

## 공시검색

### Parameter

| Name             | Type                              | DART Name        |
| ---------------- | --------------------------------- | ---------------- |
| corporation_code | `Optional[str]`                   | corp_code        |
| date_range       | `Optional[DateRange(begin, end)]` | bgn_de, end_de   |
| only_last_report | `Optional[bool]`                  | last_reprt_at    |
| type             | `Optional[DisclosureType]`        | pblntf_ty        |
| type_detail      | `Optional[str]`                   | pblntf_detail_ty |
| market           | `Optional[Market]`                | corp_cls         |
| sort             | `Optional[Sort]`                  | sort, sort_mth   |
| page             | `int` (default 1)                 | page_no          |
| limit            | `int` (default 20)                | page_count       |

### Usage

=== "Dataframe"

    ```python
    client = DataframeDisclosureClient("YOUR API KEY")

    dataframe, _, page_info = client.search(
        date_range=DateRange(begin=date(year=2021, month=1, day=1), end=datetime.now().date()),
        market=Market.KOSPI,
    )
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleDisclosureClient("YOUR API KEY")

    sequence_of_namedtuple = client.search(
        date_range=DateRange(begin=date(year=2021, month=1, day=1), end=datetime.now().date()),
        market=Market.KOSPI,
    )
    ```

=== "Dict"
    
    ```python
    client = DisclosureClient("YOUR API KEY")

    sequence_of_dict = client.search(
        date_range=DateRange(begin=date(year=2021, month=1, day=1), end=datetime.now().date()),
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
    client = DataframeDisclosureClient("YOUR API KEY")

    dataframe, _ = client.get_company_overview("00126380")
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleDisclosureClient("YOUR API KEY")
    
    sequence_of_namedtuple = client.get_company_overview("00126380")
    ```

=== "Dict"
    
    ```python
    client = DisclosureClient("YOUR API KEY")

    just_dict = client.get_company_overview("00126380")
    ```