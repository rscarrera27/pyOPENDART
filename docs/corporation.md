# Corporation

Corporation 클래스는 해당 기업의 기업개황, 사업보고서 주요정보, 재무정보, 지분공시 종합정보 등의 편리한 접근을 제공합니다. 각 메서드의 자세한 사용방법은 [각 클라이언트별 문서](./clients/disclosure.md) 를 참조하시기 바랍니다.

## 기업 정보 확인

```python
from pyopendart import Corporation

corp = Corporation("00126380", "YOUR API KEY")

print(corp.name)
print(corp.market_info)
print(corp.company_info)
```
```
{'ko': '삼성전자(주)', 'en': 'SAMSUNG ELECTRONICS CO,.LTD', 'stock': '삼성전자'}
{'name': '삼성전자', 'code': '005930', 'market': KOSPI}
{'corporation_code': '00126380', 'corporation_name': '삼성전자(주)', 'corporation_name_en': 'SAMSUNG ELECTRONICS CO,.LTD', 'stock_name': '삼성전자', 'stock_code': '005930', 'representative': '김기남, 김현석, 고동진', 'market': KOSPI, 'corporation_registration_number': 1301110006246, 'taxpayer_registration_number': 1248100998, 'address': '경기도 수원시 영통구  삼성로 129 (매탄동)', 'homepage_url': 'www.sec.co.kr', 'ir_url': '', 'phone_number': '031-200-1114', 'fax_number': '031-200-7538', 'industry_code': 264, 'establishment_date': datetime.date(1969, 1, 13), 'ending_month_of_fiscal_year': 12}
```

## 사업보고서 주요정보, 재무정보, 지분공시 종합정보 접근

기업코드 파라미터가 없는 것을 제외하고는 각 정보의 데이터프레임 클라이언트와 동일하게 사용할 수 있습니다.

```python
from pyopendart import Corporation
from pyopendart.enums import ReportType

corp = Corporation("00126380", "YOUR API KEY")

df, meta = corp.get_financial_statements_of_major_accounts(business_year=2019, report_type=ReportType.Q1)
```