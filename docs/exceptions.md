# Exceptions

클라이언트들은 올바르지 않은 요청 인자와 함께 사용되었거나, DART 서버의 에러 등에 의해 예외를 발생시킬 수 있습니다.

DART에서 문서화되어 있는 알려진 예외들은 아래의 예외 클래스들을 사용합니다. 기타 알려지지 않은 예외나 정의되지 않은 오류를 받았을 때에는 `pyopendart.exceptions.UnknownError` 예외를 발생시킵니다.

## 알려진 예외들

| Exception Class                          | Code |
| ---------------------------------------- | ---- |
| `pyopendart.exceptions.UnregisteredKey`  | 010  |
| `pyopendart.exceptions.UnusableKey`      | 011  |
| `pyopendart.exceptions.Empty`            | 013  |
| `pyopendart.exceptions.RateLimited`      | 020  |
| `pyopendart.exceptions.InvalidParameter` | 100  |
| `pyopendart.exceptions.UnderMaintenance` | 800  |


