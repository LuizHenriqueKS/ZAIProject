from ..base._processor import Processor
from typing import Literal


class AutoPadding1D(Processor):

  def __init__(self, direction: Literal['left', 'right', 'same'] = 'same', length=None, value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.direction = direction
    self.value = value
    self.length = length

  def scale(self, data, project, params=None):
    self.updateLength(project, len(data))
    self.updateValue(project, data)
    return self.apply(data, project)

  def apply(self, data, project, params=None):
    length = self.getLength(project)
    value = self.getValue(project)
    result = [*data]
    while length > len(result):
      if self.direction == 'right':
        result.append(value)
      elif self.direction == 'left':
        result.insert(0, value)
      elif self.direction == 'same':
        result.append(value)
        if length > len(result):
          result.insert(0, value)
      else:
        raise ValueError(self.direction)
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
    dataRecorder.record('length', self.length)

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
      if self.value != None:
        return self.value
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
    if self.length != None:
      return self.length
    try:
      currentLength = self.getSharedData(project)['length']
      if currentLength == None:
        return self.length
      return currentLength
    except KeyError:
      return None
