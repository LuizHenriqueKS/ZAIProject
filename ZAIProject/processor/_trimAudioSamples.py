from ..base._processor import Processor
from ..utility import applyRuleOf3
import math


class TrimAudioSamples(Processor):

  def __init__(self, bits=8, distance=2, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.bits = bits
    self.distance = abs(distance)
    self.range = self.buildRange()

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    self.trimStart(data)
    self.trimEnd(data)
    return data

  def trimStart(self, data):
    while len(data) > 1:
      if self.canTrimValue(data[0]) or self.canTrimValue(data[1]):
        data = data[1:]
      else:
        break

  def trimEnd(self, data):
    while len(data) > 1:
      if self.canTrimValue(data[-1]) or self.canTrimValue(data[-2]):
        data = data[:-1]
      else:
        break

  def canTrimValue(self, value):
    return value >= self.range[0] and value <= self.range[1]

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('bits', self.bits)
    dataRecorder.record('distance', self.distance)

  def buildRange(self):
    maxInput = math.pow(2, self.bits) - 1
    middle = math.pow(2, self.bits - 1)
    result_min = middle - self.distance
    result_max = middle + self.distance
    result_min = applyRuleOf3(result_min, 0, maxInput, -1, 1)
    result_max = applyRuleOf3(result_max, 0, maxInput, -1, 1)
    return result_min, result_max
