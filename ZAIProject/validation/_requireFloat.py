from ._isFloat import isFloat
from ..error._unexpectedTypeError import UnexpectedTypeError


def requireFloat(data):
    if not isFloat(data):
        raise UnexpectedTypeError(data, float)
