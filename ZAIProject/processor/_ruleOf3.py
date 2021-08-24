from ..base._processor import Processor
from ..utility import applyRuleOf3


class RuleOf3(Processor):

  def __init__(self, minInput, maxInput, minOutput, maxOutput, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.minInput = minInput
    self.maxInput = maxInput
    self.minOutput = minOutput
    self.maxOutput = maxOutput

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    return applyRuleOf3(data, self.minInput, self.maxInput, self.minOutput, self.maxOutput)

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    return RuleOf3(minInput=self.minOutput, maxInput=self.maxOutput, minOutput=self.minInput, maxOutput=self.maxInput)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('minInput', self.minInput)
    dataRecorder.record('maxInput', self.maxInput)
    dataRecorder.record('minOutput', self.minOutput)
    dataRecorder.record('maxOutput', self.maxOutput)
