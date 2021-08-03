def convertIndexToClass(index, length=None):
    result = []
    if length == None:
        length = index + 1
    for i in range(0, length):
        if i == index:
            result.append(1)
        else:
            result.append(0)
    return result
