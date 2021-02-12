# 고급 데이터프레임 클라이언트 옵션

데이터프레임 클라이언트는 데이터 변환, 필드 이름 변경, 인덱스 수정등의 처리를 자동으로 수행합니다. 만약 모종의 이유로 특정 처리가 되지 않은 데이터를 얻고 싶다면 데이터프레임 클라이언트들이 공통으로 제공하는 파라미터인 `convert_data`, `rename_fields`, `set_index` 를 조작하여 특정 처리 단계를 건너뛸 수 있습니다. (일부 데이터프레임 클라이언트들은 몇가지 옵션이 제공되지 않을 수도 있습니다.)


```python
def some_datframe_client_method(
    self,
    ...
    *,
    convert_data: bool = True,
    rename_fields: bool = True,
    set_index: bool = True,
): ...
```

## Convert Data

기본적으로 OPEN DART 응답은 문자열로 제공되기 때문에 숫자 데이터 등에 대해 자동으로 데이터 변환을 시도합니다. `False` 로 설정되면 데이터 자동 변환을 건너뜁니다.

## Rename Fields

기본적으로 OPEN DART 응답의 축약된 필드 이름을 좀더 읽기 쉬운 형태로 변경합니다. `False` 로 설정되면 필드 이름 변경을 건너뜁니다. 


## Set Index

기본적으로 OPEN DART 응답에 대해 인덱스를 만듭니다 `False` 로 설정되면 인덱스를 만들지 않습니다.
