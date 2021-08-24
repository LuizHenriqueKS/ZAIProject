from logging import exception
from ..base._processor import Processor
from typing import Literal


class Eraser2D(Processor):

  def __init__(self, direction: Literal['left', 'right', 'same'], value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.direction = direction
    if value == None:
      self.value = None
    elif isinstance(value, list):
      self.value = value
    else:
      self.value = [value]

  def scale(self, data, project, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    try:
      result = data
      value = self.getValue(data)
      if self.direction == 'same' or self.direction == 'left':
        while self.isValueVector(result[0], value):
          result = result[1:]
      if self.direction == 'same' or self.direction == 'right':
        while self.isValueVector(result[-1], value):
          result = result[:-1]
      return result
    except ValueError:
      return data

  def isValueVector(self, vector, value):
    for i in vector:
      if i != value:
        return False
    return True

  def getValue(self, project):
    if self.value != None:
      return self.value
    value = self.getSharedData(project)['value']
    if isinstance(value, list):
      return value
    else:
      return [value]

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._autoPadding1D import AutoPadding1D
    return AutoPadding1D(direction=self.direction, value=self.value, sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('direction', self.direction)
    dataRecorder.record('value', self.value)
