from ..base._processor import Processor


class IndexToCategorical(Processor):

  def __init__(self, length=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.length = length

  def scale(self, data, project, params=None):
    result = self.apply(data, project, params)
    self.updateLength(project, len(result))
    return result

  def apply(self, data, project, params=None):
    length = max(self.getLength(project), data + 1)
    result = []
    for i in range(length):
      if i == data:
        result.append(1)
      else:
        result.append(0)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('length', self.length)

  def updateLength(self, project, length):
    currentLength = self.getLength(project)
    if currentLength == None or currentLength < length:
      self.setLength(project, length)

  def setLength(self, project, length):
    self.getSharedData(project)['length'] = length

  def getLength(self, project):
    if self.length != None:
      return self.length
    try:
      currentLength = self.getSharedData(project)['length']
      if currentLength == None:
        return 1
      return currentLength
    except KeyError:
      return 1
