from ..base._processor import Processor


class OutputLength(Processor):

  def __init__(self, index, returnSequence=False, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)
    self.index = index
    self.returnSequence = True

  def scale(self, data, project, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    if len(project.modelInfo.output) == 0:
      outputLength = 1
    else:
      outputLength = project.modelInfo.output[self.index].shape[0]
      if outputLength is None:
        outputLength = 1
    if self.returnSequence:
      return [i for i in range(outputLength)]
    return outputLength

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('index', self.index)
    dataRecorder.record('returnSequence', self.returnSequence)
