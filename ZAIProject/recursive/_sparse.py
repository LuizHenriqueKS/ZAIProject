from tensorflow.python.ops.gen_array_ops import Reverse
from ..base._recursive import Recursive
from typing import List
from ..processor._reverseSparse import ReverseSparse


class Sparse(Recursive):

  def __init__(self, contextShape: List[int]):
    super().__init__()
    self.contextShape = contextShape
    self.reverseSparseProcessor = ReverseSparse()

  def convertOutputToContext(self, output):
    result = []
    for ioOutput in output:
      result.append(self.reverseSparseProcessor.apply(ioOutput))
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
