# pyOPENDART - OPEN DART Python API (for Humans)

전자공시시스템 API 를 편리하게 사용하기 위해 저수준 HTTP API부터 데이터프레임을 리턴하는 고수준 API 등 각종 편리한 API와 유틸리티들을 제공합니다.

### Disclaimer
> 본 소프트웨어는 금융감독원의 전자공시시스템 OPEN API 를 추가적으로 가공하고 부가기능을 제공하는 소프트웨어로써 MIT 라이선스에 따라 저자 또는 저작권자는 소프트웨어와 소프트웨어와 연관되어 발생하는 문제에 대해 책임을 지지 않습니다.
> 
> OPEN DART API에 관한 정보는 opendart.fss.or.kr 를 참조하시기 바랍니다.

## Installation

```shell
pip install pyopendart
```

## What is DART?

> 전자공시시스템(DART ; Data Analysis, Retrieval and Transfer System)은 상장법인 등이 공시서류를 인터넷으로 제출 하고, 투자자 등 이용자는 제출 즉시 인터넷을 통해 조회할 수 있도록 하는 종합적 기업공시 시스템입니다.
>
> by [dart.fss.or.kr - DART소개](http://dart.fss.or.kr/introduction/content1.do)

## What is OPEN DART?

> DART에 공시되고있는 공시보고서 원문 등을 오픈API를 통해 활용할 수 있습니다. 활용을 원하시는 누구든지(개인, 기업, 기관 등) 이용하실 수 있습니다.
>
> by [opendart.fss.or.kr - 오픈API 소개](https://opendart.fss.or.kr/intro/main.do)

## Features

* OPEN API 데이터프레임, 딕셔너리 클라이언트
    * dart의 축약된 필드명을 자세한 한글, 영어 필드명으로 변환
    * 날짜, 숫자등에 대해 데이터 타입 변환
* 공시원문, 재무재표 등 원본파일 다운로드 클라이언트
* 로우레벨 OPEN API HTTP 클라이언트
    * 커넥션 풀, 타임아웃등 네트워크 옵션 조정 기능 제공
    * xml, json, zip 리소스 접근 메서드 제공
* 편리하고 타입 정의된 클라이언트 인터페이스들
    * 요청 인자 중 공시유형등의 필드에 대한 Enum 제공
    * 예외 클래스 제공
* 개발가이드에 나와있는 출력설명란의 출력과 설명의 매핑 제공 (비고 등)

## Usage

[https://pyopendart.seonghyeon.dev/](https://pyopendart.seonghyeon.dev/) 에서 자세한 문서를 확인할 수 있습니다.

## License
This project is licensed under the terms of the MIT license.