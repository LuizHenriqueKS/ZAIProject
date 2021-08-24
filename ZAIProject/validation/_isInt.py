import numpy as np


def isInt(data):
  return isinstance(data, int) or type(data).__name__ == 'int32' or type(data).__name__ == 'int64'
