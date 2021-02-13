# OPEN DART Python API (for Humans)

전자공시시스템 API 를 편리하게 사용하기 위해 딕셔너리를 리턴하는 저수준 API부터 데이터프레임, 네임드튜플 등을 리턴하는 고수준 API 등 각종 편리한 API들을 제공합니다.

!!! Disclimer
    * 본 소프트웨어는 금융감독원의 전자공시시스템 OPEN API 를 추가적으로 가공하고 부가기능을 제공하는 소프트웨어로써 MIT 라이선스에 따라 저자 또는 저작권자는 소프트웨어와 소프트웨어와 연관되어 발생하는 문제에 대해 책임을 지지 않습니다.
    * OPEN DART API에 관한 정보는 opendart.fss.or.kr 를 참조하시기 바랍니다.

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

* OPEN API 데이터프레임 클라이언트
    * 읽기 쉬운 형태로 필드명 자동 변환
    * 숫자, 시간등 일부 데이터 타입 자동 변환
    * 공시 양식에 맞추어 자동 인덱싱
* OPEN API 네임드튜플 클라이언트
* OPEN API 딕셔너리 클라이언트
* 편리하고 타입 정의된 클라이언트 인터페이스
* 쉽게 해당 기업의 정보를 받아오기 위한 법인 클래스 제공

## License
This project is licensed under the terms of the MIT license.