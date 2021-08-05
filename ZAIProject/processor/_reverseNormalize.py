from ..base._processor import Processor
from ..utility._applyRuleOf3 import applyRuleOf3


class ReverseNormalize(Processor):

  def __init__(self, minOutput=0, maxOutput=1, sharedDataId=None, reverse=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)
    self.minOutput = minOutput
    self.maxOutput = maxOutput

  def scale(self, data, project, params=None):
    sharedData = self.getSharedData(project)
    if 'minInput' not in sharedData or sharedData.minInput > data:
      sharedData.minInput = data
    if 'maxInput' not in sharedData or sharedData.maxInput < data:
      sharedData.maxInput = data
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    sharedData = self.getSharedData(project)
    result = applyRuleOf3(data, self.minOutput, self.maxOutput,
                          sharedData['minInput'], sharedData['maxInput'])
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._normalize import Normalize
    return Normalize(self.minOutput, self.maxOutput, self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('minOutput', self.minOutput)
    dataRecorder.record('maxOutput', self.maxOutput)
