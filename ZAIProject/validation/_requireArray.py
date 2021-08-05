from ..error._unexpectedTypeError import UnexpectedTypeError
from ._isArray import isArray


def requireArray(data):
  if not isArray(data):
    raise UnexpectedTypeError(data, list)
