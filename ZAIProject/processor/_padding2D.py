from ..base._processor import Processor
from typing import Literal
from ..utility._getShape import getShape
from ..utility._getMaxShape import getMaxShape


class Padding2D(Processor):

  def __init__(self, leftLength, rightLength, shape=None, value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.leftLength = leftLength
    self.rightLength = rightLength
    self.value = value
    self.shape = shape

  def scale(self, data, project, params=None):
    self.updateShape(project, data)
    self.updateValue(project, data)
    return self.apply(data, project)

  def apply(self, data, project, params=None):
    value = self.getValue(project)
    shape = self.getShape(project)
    if hasattr(data, 'tolist'):
      result = data.tolist()
    else:
      result = data
    for _ in range(self.rightLength):
      result.append(self.buildValuesVector(shape, value))
    for _ in range(self.leftLength):
      result.insert(0, self.buildValuesVector(shape, value))
    return result

  def buildValuesVector(self, shape, value):
    result = []
    for _ in range(shape[1]):
      result.append(value)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    end = None
    if self.rightLength != None and self.rightLength != 0:
      end = - self.rightLength
    from ._slice1D import Slice1D
    return Slice1D(start=self.leftLength, end=end, sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('leftLength', self.leftLength)
    dataRecorder.record('rightLength', self.rightLength)
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
      return currentShape
    except KeyError:
      return None
