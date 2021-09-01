from ..base._processor import Processor
from typing import Literal
from ..utility._getShape import getShape
from ..utility._getMaxShape import getMaxShape


class AutoPadding2D(Processor):

  def __init__(self, direction: Literal['left', 'right', 'same'] = 'same', shape=None, value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.direction = direction
    self.value = value
    self.shape = shape

  def scale(self, data, project, params=None):
    self.updateShape(project, data)
    self.updateValue(project, data)
    return self.apply(data, project)

  def apply(self, data, project, params=None):
    shape = self.getShape(project)
    value = self.getValue(project)
    result = data
    if type(result).__name__ == 'ndarray':
      result = result.tolist()
    while shape[0] > len(result):
      if self.direction == 'right':
        result.append(self.buildValuesVector(shape, value))
      elif self.direction == 'left':
        result.insert(0, self.buildValuesVector(shape, value))
      elif self.direction == 'same':
        result.append(self.buildValuesVector(shape, value))
        if shape[0] > len(result):
          result.insert(0, self.buildValuesVector(shape, value))
      else:
        raise ValueError(self.direction)
    return result

  def buildValuesVector(self, shape, value):
    result = []
    for _ in range(shape[1]):
      result.append(value)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._eraser2D import Eraser2D
    return Eraser2D(direction=self.direction, value=self.value, sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('direction', self.direction)
    dataRecorder.record('value', self.value)
    dataRecorder.record('shape', self.shape)

  def updateValue(self, project, data):
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

  def updateShape(self, project, data):
    if self.shape == None:
      currentShape = self.getShape(project)
      shape = getShape(data)
      if currentShape == None:
        self.setShape(project, shape)
      else:
        self.setShape(project, getMaxShape(shape, currentShape))

  def setShape(self, project, shape):
    self.getSharedData(project)['shape'] = shape

  def getShape(self, project):
    if self.shape != None:
      return self.shape
    try:
      currentShape = self.getSharedData(project)['shape']
      if currentShape is None:
        return self.shape
      return currentShape
    except KeyError:
      return None
