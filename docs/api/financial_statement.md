# 상장기업 재무정보

## Import

=== "Dataframe"

    ```python
    from pyopendart.api.dataframe import FinancialStatementApi
    from pyopendart.enums import ReportType, FinancialStatementDivision, FinancialStatementTypeDetail
    ```

=== "Dict"
    
    ```python
    from pyopendart.api.dict import FinancialStatementApi
    from pyopendart.enums import ReportType, FinancialStatementDivision, FinancialStatementTypeDetail
    ```

## 단일ㆍ다중회사 주요계정
### Parameter

| Name              | Type         | DART Name  |
| ----------------- | ------------ | ---------- |
| corporation_codes | `List[str]`  | corp_code  |
| business_year     | `int`        | bsns_year  |
| report_type       | `ReportType` | reprt_code |

### Usage

=== "Dataframe"

    ```python
    api = FinancialStatementApi("YOUR API KEY")

    df = api.get_financial_statements_of_major_accounts(
        corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1
    )
    ```

=== "Dict"
    
    ```python
    api = FinancialStatementApi("YOUR API KEY")

    financial_statements_of_major_accounts = api.get_financial_statements_of_major_accounts(
        corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1
    )
    ```

## 단일회사 전체 재무제표
### Parameter

| Name                         | Type                                     | DART Name  |
| ---------------------------- | ---------------------------------------- | ---------- |
| corporation_codes            | `List[str]`                              | corp_code  |
| business_year                | `int`                                    | bsns_year  |
| report_type                  | `ReportType`                             | reprt_code |
| financial_statement_division | `Union[FinancialStatementDivision, str]` | fs_div     |

### Usage

=== "Dataframe"

    ```python
    api = FinancialStatementApi("YOUR API KEY")

    df = api.get_full_financial_statements(
        corporation_code="00293886", business_year=2019, report_type=ReportType.Q1
    )
    ```

=== "Dict"
    
    ```python
    api = FinancialStatementApi("YOUR API KEY")

    full_financial_statements = api.get_full_financial_statements(
        corporation_code="00293886", business_year=2019, report_type=ReportType.Q1
    )
    ```

## XBRL택소노미 재무제표양식
### Parameter

| Name                              | Type                                       | DART Name |
| --------------------------------- | ------------------------------------------ | --------- |
| detailed_financial_statement_type | `Union[FinancialStatementTypeDetail, str]` | sj_div    |

### Usage

=== "Dataframe"

    ```python
    api = FinancialStatementApi("YOUR API KEY")
    
    df = api.get_xbrl_taxonomies(FinancialStatementTypeDetail.BS1)  # or "BS1" in string
    ```

=== "Dict"
    
    ```python
    api = FinancialStatementApi("YOUR API KEY")

    xbrl_taxonomies = api.get_xbrl_taxonomies(FinancialStatementTypeDetail.BS1)
    ```

## 재무제표 원본파일(XBRL) 다운로드

재무제표 원본파일 (XBRL) 응답을 자동으로 압축 해제에 지정한 경로에 저장합니다.

### Parameter

| Name             | Type         | DART Name  |
| ---------------- | ------------ | ---------- |
| corporation_code | `str`        | corp_code  |
| report_type      | `ReportType` | reprt_code |

### Usage

```python
api = FinancialStatementApi("YOUR API KEY")

api.get_xbrl_document("20190401004781", ReportType.ANNUAL, "./temp")
```