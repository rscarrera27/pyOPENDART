# 지분공시 종합정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.clients.dataframe.shareholder import DataframeShareholderReportClient
    ```

=== "Namedtuple"
    
    ```python
    from pyopendart.clients.namedtuple.shareholder import NamedtupleShareholderReportClient
    ```

=== "Dict"
    
    ```python
    from pyopendart.clients.dict.shareholder import ShareholderReportClient
    ```

## Parameter

| Name             | Type  | DART Name |
| ---------------- | ----- | --------- |
| corporation_code | `str` | corp_code |


## 대량보유 상황보고

=== "Dataframe"

    ```python
    client = DataframeShareholderReportClient("YOUR API KEY")

    df, meta = client.get_major_shareholder_reports(corporation_code="00126380")
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleShareholderReportClient("YOUR API KEY")

    major_shareholder_report = client.get_major_shareholder_reports(corporation_code="00126380")
    ```

=== "Dict"
    
    ```python
    client = ShareholderReportClient("YOUR API KEY")

    major_shareholder_report = client.get_major_shareholder_reports(corporation_code="00126380")
    ```

## 임원ㆍ주요주주 소유보고

=== "Dataframe"

    ```python
    client = DataframeShareholderReportClient("YOUR API KEY")

    df, meta = client.get_executive_shareholder_reports(corporation_code="00126380")
    ```

=== "Namedtuple"
    
    ```python
    client = NamedtupleShareholderReportClient("YOUR API KEY")

    executive_shareholder_reports = client.get_executive_shareholder_reports(corporation_code="00126380")
    ```

=== "Dict"
    
    ```python
    client = ShareholderReportClient("YOUR API KEY")

    executive_shareholder_reports = client.get_executive_shareholder_reports(corporation_code="00126380")
    ```