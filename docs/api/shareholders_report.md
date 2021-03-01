# 지분공시 종합정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.api.dataframe import ShareholdersReportApi
    ```

=== "Dict"
    
    ```python
    from pyopendart.api.dataframe import ShareholdersReportApi
    ```

## Parameter

| Name             | Type  | DART Name |
| ---------------- | ----- | --------- |
| corporation_code | `str` | corp_code |


## 대량보유 상황보고

=== "Dataframe"

    ```python
    api = ShareholdersReportApi("YOUR API KEY")

    df = api.get_major_shareholder_reports(corporation_code="00126380")
    ```

=== "Dict"
    
    ```python
    api = ShareholdersReportApi("YOUR API KEY")

    major_shareholder_report = api.get_major_shareholder_reports(corporation_code="00126380")
    ```

## 임원ㆍ주요주주 소유보고

=== "Dataframe"

    ```python
    api = ShareholdersReportApi("YOUR API KEY")

    df = api.get_executive_shareholder_reports(corporation_code="00126380")
    ```

=== "Dict"
    
    ```python
    api = ShareholdersReportApi("YOUR API KEY")

    executive_shareholder_reports = api.get_executive_shareholder_reports(corporation_code="00126380")
    ```