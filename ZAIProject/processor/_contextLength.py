from ..base._processor import Processor


class ContextLength(Processor):

  def __init__(self, contextIndex: int, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.contextIndex = contextIndex

  def scale(self, data, project, params):
    return self.apply(data, project, params)

  def apply(self, data, project, params):
    if len(params.context) == 0:
      return [0]
    return [len(params.context[self.contextIndex])]

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('contextIndex', self.contextIndex)
