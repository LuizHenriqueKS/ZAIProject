from numpy.core.fromnumeric import transpose
from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa


class TreatRepetitions(Processor):

  def __init__(self, endValue=0, returnSequence=True, returnRepetitions=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.returnSequence = returnSequence
    self.returnRepetitions = returnRepetitions
    self.endValue = endValue

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    sequence = []
    repetitions = []
    lastValue = None
    repetition = 0
    for i in data:
      if i == lastValue:
        repetition += 1
      else:
        if lastValue != None:
          sequence.append(lastValue)
          repetitions.append(repetition)
        lastValue = i
        repetition = 0
    if lastValue is None:
      sequence.append(self.endValue)
    else:
      sequence.append(lastValue)
    repetitions.append(repetition)
    if self.returnSequence and self.returnRepetitions:
      return [sequence, repetitions]
    elif self.returnSequence:
      return sequence
    elif self.returnRepetitions:
      return repetitions

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('returnSequence', self.returnSequence)
    dataRecorder.record('returnRepetitions', self.returnRepetitions)
    dataRecorder.record('endValue', self.endValue)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._reverseTreatRepetitions import ReverseTreatRepetitions
      return ReverseTreatRepetitions(endValue=self.endValue, returnSequence=self.returnSequence, returnRepetitions=self.returnRepetitions, sharedDataId=self.sharedDataId)
