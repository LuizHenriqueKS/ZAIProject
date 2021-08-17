from logging import exception
from ..base._processor import Processor
from typing import Literal


class Trim1D(Processor):

  def __init__(self, direction: Literal['left', 'right', 'both'] = 'both', value=None, sharedDataId=None, reverse=None, name=None):
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
    result = [x for x in data]
    values = self.getValue(project)
    if self.direction == 'both' or self.direction == 'left':
      for i in range(0, len(result)):
        if result[0] in values:
          result.pop(0)
        else:
          break
    if self.direction == 'both' or self.direction == 'right':
      for i in range(0, len(result)):
        if result[-1] in values:
          result.pop()
        else:
          break
    return result

  def getValue(self, project):
    if self.value != None:
      return self.value
    value = self.getSharedData(project)['value']
    if isinstance(value, list):
      return value
    else:
      return [value]

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('direction', self.direction)
    dataRecorder.record('value', self.value)
