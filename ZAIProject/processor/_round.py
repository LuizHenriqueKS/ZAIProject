from ..base._processor import Processor
from ..validation._requireNumber import requireNumber


class Round(Processor):

  def __init__(self, numOfDecimals: int = None, reverse: Processor = None, sharedDataId=None, name=None):
    super().__init__(reverse=reverse, sharedDataId=sharedDataId, name=name)
    self.numOfDecimals = numOfDecimals

  def scale(self, data, project=None, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    requireNumber(data)
    return round(data, self.numOfDecimals)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('numOfDecimals', self.numOfDecimals)
