from ..base._processor import Processor
from ..utility._applyRuleOf3 import applyRuleOf3


class Normalize(Processor):

  def __init__(self, minOutput=0, maxOutput=1, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)
    self.minOutput = minOutput
    self.maxOutput = maxOutput
    self.name = name

  def scale(self, data, project, params=None):
    sharedData = self.getSharedData(project)
    if 'minInput' not in sharedData or sharedData['minInput'] > data:
      sharedData['minInput'] = data
    if 'maxInput' not in sharedData or sharedData['maxInput'] < data:
      sharedData['maxInput'] = data
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    sharedData = self.getSharedData(project)
    if sharedData['minInput'] == sharedData['maxInput']:
      return 0
    result = applyRuleOf3(data, sharedData['minInput'], sharedData['maxInput'],
                          self.minOutput, self.maxOutput)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._reverseNormalize import ReverseNormalize
    return ReverseNormalize(self.minOutput, self.maxOutput, self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('minOutput', self.minOutput)
    dataRecorder.record('maxOutput', self.maxOutput)
