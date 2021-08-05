from ..base._processor import Processor
from typing import Literal


class AutoPadding1D(Processor):

  def __init__(self, direction: Literal['left', 'right'] = 'right', value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.direction = direction
    self.value = value

  def scale(self, data, project, params=None):
    self.updateLength(project, len(data))
    self.updateValue(project, data)
    return data

  def apply(self, data, project, params=None):
    length = self.getLength(project)
    value = self.getValue(project)
    result = [*data]
    while length > len(result):
      result.append(value)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._eraser1D import Eraser1D
    return Eraser1D(direction=self.direction, value=self.value, sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('direction', self.direction)
    dataRecorder.record('value', self.value)

  def updateValue(self, project, data):
    if len(data) > 0:
      if self.value == None:
        maxValue = max(data)
        currentValue = self.getValue(project)
        if currentValue == None or currentValue <= maxValue:
          self.setValue(project, maxValue + 1)

  def setValue(self, project, value):
    self.getSharedData(project)['value'] = value

  def getValue(self, project):
    try:
      return self.getSharedData(project)['value']
    except KeyError:
      return None

  def updateLength(self, project, length):
    currentLength = self.getLength(project)
    if currentLength == None or currentLength < length:
      self.setLength(project, length)

  def setLength(self, project, length):
    self.getSharedData(project)['length'] = length

  def getLength(self, project):
    try:
      currentLength = self.getSharedData(project)['length']
      if currentLength == None:
        return self.length
      return currentLength
    except KeyError:
      return None
