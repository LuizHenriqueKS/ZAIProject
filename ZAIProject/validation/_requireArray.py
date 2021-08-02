from ..error._unexpectedTypeError import UnexpectedTypeError


def requireArray(data):
    if (not isinstance(data, list)):
        raise UnexpectedTypeError(data, list)
