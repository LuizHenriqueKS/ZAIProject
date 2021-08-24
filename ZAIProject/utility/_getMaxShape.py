def getMaxShape(*argv):
  if len(argv) == 0:
    return []
  else:
    result = None
    for i in range(0, len(argv)):
      if argv[i] != None:
        if result == None:
          result = [*argv[i]]
        else:
          for j in range(len(argv[i])):
            result[j] = max(argv[i][j], result[j])
    return result
