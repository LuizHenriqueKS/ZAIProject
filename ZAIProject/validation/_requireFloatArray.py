from ._requireArray import requireArray
from ._requireFloat import requireFloat


def requireFloatArray(data):
    requireArray(data)
    if len(data) > 0:
        requireFloat(data[0])
