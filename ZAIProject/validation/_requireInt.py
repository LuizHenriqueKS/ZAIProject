from ..error._unexpectedTypeError import UnexpectedTypeError


def requireInt(data):
    if (not isinstance(data, int)):
        raise UnexpectedTypeError(data, int)
