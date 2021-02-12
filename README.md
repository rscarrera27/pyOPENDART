# pyOPENDART - OPEN DART Python API (for Humans)

인간친화적인 전자공시시스템 DART 파이썬 API

전자공시시스템 API 를 편리하게 사용하기 위해 딕셔너리를 리턴하는 저수준 API부터 데이터프레임, 네임드튜플 등을 리턴하는 고수준 API 등 각종 편리한 API가 구현되어 있습니다.

### Disclimer
* 본 소프트웨어는 금융감독원의 전자공시시스템 OPEN API 를 추가적으로 가공하고 부가기능을 제공하는 소프트웨어로써 MIT 라이선스에 따라 저자 또는 저작권자는 소프트웨어와 소프트웨어와 연관되어 발생하는 문제에 대해 책임을 지지 않습니다.
* OPEN DART API에 관한 정보는 opendart.fss.or.kr 를 참조하시기 바랍니다.

## What is DART?

> 전자공시시스템(DART ; Data Analysis, Retrieval and Transfer System)은 상장법인 등이 공시서류를 인터넷으로 제출 하고, 투자자 등 이용자는 제출 즉시 인터넷을 통해 조회할 수 있도록 하는 종합적 기업공시 시스템입니다.
>
> by [dart.fss.or.kr - DART소개](http://dart.fss.or.kr/introduction/content1.do)

## What is OPEN DART?

> DART에 공시되고있는 공시보고서 원문 등을 오픈API를 통해 활용할 수 있습니다. 활용을 원하시는 누구든지(개인, 기업, 기관 등) 이용하실 수 있습니다.
>
> by [opendart.fss.or.kr - 오픈API 소개](https://opendart.fss.or.kr/intro/main.do)

## Features

* OPEN API 데이터프레임 클라이언트
  * 읽기 쉬운 형태로 필드명 자동 변환
  * 숫자, 시간등 일부 데이터 타입 자동 변환
  * 재무재표 양식대로 자동 인덱싱
* OPEN API 네임드튜플 클라이언트
* OPEN API 딕셔너리 클라이언트
* 편리하고 타입 정의된 클라이언트 인터페이스
* ~~해당 법인을 조회하고 정보를 편리하게 받아올 수 있는 법인 객체~~ (구현 예정)

## Todos
* 테스트코드
* 법인 객체
* 데이터 다운로드 API
* 문서화

## Usage

### 공시정보 API (Dataframe)

```python
from datetime import date, datetime
from pyopendart.clients.dataframe.disclosure import DataframeDisclosureClient
from pyopendart.clients.dict.disclosure import DateRange
from pyopendart.enums import Market

df_client = DataframeDisclosureClient("YOUR API KEY")

# 공시검색
df_client.search(
    date_range=DateRange(begin=date(year=2021, month=1, day=1), end=datetime.now().date()),
    market=Market.KOSPI,
)
# 기업개황
df_client.get_company_overview("00126380")
```

### 사업보고서 API (Dataframe)

```python
from pyopendart.clients.dataframe.business_report import DataframeBusinessReportClient
from pyopendart.enums import ReportType

df_client = DataframeBusinessReportClient("YOUR API KEY")

# 증자(감자) 현황
df_client.get_changes_in_equity(corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL)
# 배당에 관한 사항
df_client.get_dividend_info(corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL)
# 자기주식 취득 및 처분 현황
df_client.get_treasury_shares_status(corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL)
# 최대주주 현황
df_client.get_major_shareholders(corporation_code="00293886", business_year=2018, report_type=ReportType.ANNUAL)
# 최대주주 변동 현황
df_client.get_changes_in_major_shareholder(corporation_code="00356361", business_year=2018, report_type=ReportType.ANNUAL)
# 소액주주 현황
df_client.get_minority_shareholders_status(corporation_code="00293886", business_year=2019, report_type=ReportType.Q1)
# 임원 현황
df_client.get_executives(corporation_code="00126380", business_year=2019, report_type=ReportType.Q1)
# 직원 현황
df_client.get_employment_status(corporation_code="00126380", business_year=2019, report_type=ReportType.Q1)
# 이사ㆍ감사의 개인별 보수 현황	
df_client.get_individual_executive_compensation_status(corporation_code="00126380", business_year=2019, report_type=ReportType.ANNUAL)
# 이사ㆍ감사 전체의 보수현황	
df_client.get_executive_compensation_status(corporation_code="00126380", business_year=2019, report_type=ReportType.ANNUAL)
# 개인별 보수지급 금액(5억이상 상위5인)
df_client.get_top_5_individual_executive_compensation(corporation_code="00126380", business_year=2019, report_type=ReportType.ANNUAL)
# 타법인 출자현황	
df_client.get_investment_in_other_corporations(corporation_code="00293886", business_year=2019, report_type=ReportType.ANNUAL)
```

### 재무재표 API (Dataframe)

```python
from pyopendart.clients.dataframe.financial_information import DataframeFinancialInformationClient
from pyopendart.enums import ReportType

df_client = DataframeFinancialInformationClient("e32e1ae12ac94446f3133bc0b7e42491b0cde4a3")

# 단일회사,다중회사 주요계정	
df_client.get_financial_statements_of_major_accounts(corporation_codes=["00293886", "00126380"], business_year=2019, report_type=ReportType.Q1)
# 단일회사 전체 재무재표
df_client.get_full_financial_statements(corporation_code="00293886", business_year=2019, report_type=ReportType.Q1)
# XBRL택소노미 재무제표 양식
df_client.get_xbrl_taxonomies("BS1")
```

## 지분공시 API (Dataframe)

```python
from pyopendart.clients.dataframe.shareholder import DataframeShareholderReportClient

df_client = DataframeShareholderReportClient("e32e1ae12ac94446f3133bc0b7e42491b0cde4a3")

# 대량보유 상황보고
df_client.get_major_shareholder_reports(corporation_code="00126380")
# 임원ㆍ주요주주 소유보고	
df_client.get_executive_shareholder_reports(corporation_code="00126380")
```

## License
This project is licensed under the terms of the MIT license.