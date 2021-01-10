class DartException(Exception):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message


class UnregisteredKey(DartException):
    """
    등록되지 않은 키입니다.
    """

    def __init__(self, message: str):
        super(UnregisteredKey, self).__init__("010", message)


class UnusableKey(DartException):
    """
    사용할 수 없는 키입니다. 오픈API에 등록되었으나, 일시적으로 사용 중지된 키를 통하여 검색하는 경우 발생합니다.
    """

    def __init__(self, message: str):
        super(UnusableKey, self).__init__("011", message)


class Empty(DartException):
    """
    조회된 데이타가 없습니다.
    """

    def __init__(self, message: str):
        super(Empty, self).__init__("013", message)


class RateLimited(DartException):
    """
    요청 제한을 초과하였습니다.
    일반적으로는 10,000건 이상의 요청에 대하여 이 에러 메시지가 발생되나, 요청 제한이 다르게 설정된 경우에는 이에 준하여 발생됩니다.
    """

    def __init__(self, message: str):
        super(RateLimited, self).__init__("020", message)


class InvalidParameter(DartException):
    """
    필드의 부적절한 값입니다. 필드 설명에 없는 값을 사용한 경우에 발생하는 메시지입니다.
    """

    def __init__(self, message: str):
        super(InvalidParameter, self).__init__("100", message)


class UnderMaintenance(DartException):
    """
    원활한 공시서비스를 위하여 오픈API 서비스가 중지 중입니다.
    """

    def __init__(self, message: str):
        super(UnderMaintenance, self).__init__("800", message)


class UnknownError(DartException):
    """
    정의되지 않은 오류가 발생하였습니다.
    """

    def __init__(self, message: str):
        super(UnknownError, self).__init__("900", message)
