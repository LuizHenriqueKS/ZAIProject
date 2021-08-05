def isArray(data):
  return isinstance(data, list) or type(data).__name__ == 'array' or type(data).__name__ == 'ndarray'
