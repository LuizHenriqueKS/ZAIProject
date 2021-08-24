from ..base._processor import Processor
from ..utility import applyRuleOf3
import math


class DownQualityAudioSamples(Processor):

  def __init__(self, bits=8, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.bits = bits

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    result = []
    minOutput = 0
    maxOutput = math.pow(2, self.bits) - 1
    for i in data:
      r = applyRuleOf3(i, -1, 1, minOutput, maxOutput)
      r = round(r)
      r = applyRuleOf3(r, minOutput, maxOutput, -1, 1)
      result.append(r)
    return result

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('bits', self.bits)
