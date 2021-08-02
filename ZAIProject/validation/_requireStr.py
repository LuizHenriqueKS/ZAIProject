from ..error._unexpectedTypeError import UnexpectedTypeError


def requireStr(data):
    if (not isinstance(data, str)):
        raise UnexpectedTypeError(data, str)
