from ..base._processor import Processor


class Slice1D(Processor):

  def __init__(self, start, end=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.start = start
    self.end = end

  def scale(self, data, project, params):
    return self.apply(data, project, params)

  def apply(self, data, project, params):
    if self.end != None:
      return data[self.start:self.end]
    else:
      return data[self.start:]

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('start', self.start)
    dataRecorder.record('end', self.end)
