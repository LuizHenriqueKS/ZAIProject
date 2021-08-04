def getShape(data):
  if isinstance(data, list):
    # More dimensions, so make a recursive call
    outermost_size = len(data)
    if outermost_size == 0:
      return 0
    row_shape = getShape(data[0])
    return [outermost_size, *row_shape]
  else:
    # No more dimensions, so we're done
    return []
