from ..error._unexpectedTypeError import UnexpectedTypeError
from ._isInt import isInt


def requireInt(data):
    if (not isInt(data)):
        raise UnexpectedTypeError(data, int)
