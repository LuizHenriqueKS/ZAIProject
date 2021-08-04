def getBestIndex(data):
    bestIndex = 0
    maxValue = data[0]
    for i in range(1, len(data)):
        if maxValue < data[i]:
            maxValue = data[i]
            bestIndex = i
    return bestIndex
