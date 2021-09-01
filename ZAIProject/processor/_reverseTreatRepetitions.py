from numpy.core.fromnumeric import transpose
from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa


class ReverseTreatRepetitions(Processor):

  def __init__(self, endValue=0, returnSequence=True, returnRepetitions=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.returnSequence = returnSequence
    self.returnRepetitions = returnRepetitions
    self.endValue = endValue

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    if self.returnRepetitions and self.returnSequence:
      result = []
      for value in data[0]:
        for repetition in data[1]:
          for i in range(repetition):
            result.append(value)
      return result
    else:
      return data

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('returnSequence', self.returnSequence)
    dataRecorder.record('returnRepetitions', self.returnRepetitions)
    dataRecorder.record('endValue', self.endValue)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._treatRepetitions import TreatRepetitions
      return TreatRepetitions(endValue=self.endValue, returnSequence=self.returnSequence, returnRepetitions=self.returnRepetitions, sharedDataId=self.sharedDataId)
