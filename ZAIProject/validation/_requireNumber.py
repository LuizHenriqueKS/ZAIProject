from ..error._unexpectedTypeError import UnexpectedTypeError
from ._isInt import isInt
from ._isFloat import isFloat


def requireNumber(data):
    if (not isInt(data) and not isFloat(data)):
        raise UnexpectedTypeError(data, 'number')
