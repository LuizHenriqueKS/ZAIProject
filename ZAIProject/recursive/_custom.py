from ..base._recursive import Recursive
from typing import List
from ..processor._reverseSparse import ReverseSparse


class Custom(Recursive):

  def __init__(self, processor, contextShape: List[int], maxLengthContext=0):
    super().__init__()
    self.contextShape = contextShape
    self.processor = processor
    self.maxLengthContext = maxLengthContext

  def saveData(self, dataRecorder):
    dataRecorder.record('contextShape', self.contextShape)
    dataRecorder.record('maxLengthContext', self.maxLengthContext)
    dataRecorder.record('type', type(self).__name__)
    self.processor.saveData(dataRecorder.getChild("processor"))

  def canContinuePredict(self, params):
    length = self.getContextLength(params)
    return length < self.maxLengthContext

  def inspectParams(self, params):
    length = self.getContextLength(params)
    self.maxLengthContext = max(self.maxLengthContext, length + 1)

  def getContextLength(self, params):
    length = len(params.context)
    if length > 0:
      length = len(params.context[0])
    return length

  def convertOutputToContext(self, output):
    result = []
    for ioOutput in output:
      result.append(self.processor.apply(ioOutput))
    return result

  def getOutput(self, params):
    result = []
    for io in range(0, len(params.context)):
      result.append([])
      for output in params.context[io]:
        for one in output:
          result[io].append(one)
    return result

  def splitTarget(self, target):
    hasData = True
    indexes = [0 for _ in range(0, len(self.contextShape))]
    while hasData:
      hasData = False
      loopResult = []
      for io in range(0, len(self.contextShape)):
        ioTarget = target[io]
        splitedTarget = self.splitIOTarget(io, ioTarget, indexes)
        hasData |= len(ioTarget) > indexes[io]
        loopResult.append(splitedTarget)
      yield loopResult

  def splitIOTarget(self, io: int, ioTarget, indexes: List[int]):
    index = indexes[io]
    result = []
    for i in range(0, self.contextShape[io]):
      result.append(ioTarget[index + i])
    indexes[io] = index + len(result)
    return result
