from ._requireArray import requireArray
from ._requireNumber import requireNumber


def requireNumberArray(data):
    requireArray(data)
    if len(data) > 0:
        requireNumber(data[0])
