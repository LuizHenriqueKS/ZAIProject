from logging import exception
from ..base._processor import Processor
from typing import Literal


class Eraser1D(Processor):

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
      if self.direction == 'same' or self.direction == 'left':
        value = self.getValue(project)
        while result[0] in value:
          result = result[1:]
      if self.direction == 'same' or self.direction == 'right':
        value = self.getValue(project)
        while len(result) > 0 and result[-1] in value:
          result = result[:-1]
      return result
    except ValueError:
      return data

  def findIndex(self, project, data, direction):
    value = self.getValue(project)
    index = None
    for val in value:
      if direction == 'left':
        cIndex = self.index(val, data)
        if index == None or index < cIndex:
          index = cIndex
      elif direction == 'right':
        cIndex = self.lastIndex(val, data)
        if index == None or index > cIndex:
          index = cIndex
      else:
        raise NotImplementedError()
    return index

  def index(self, val, data):
    for i in range(0, len(data)):
      v = data[i]
      if v == val:
        return i

  def lastIndex(self, val, data):
    for i in range(0, len(data)):
      v = data[len(data) - 1 - i]
      if v == val:
        return len(data) - 1 - i

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
