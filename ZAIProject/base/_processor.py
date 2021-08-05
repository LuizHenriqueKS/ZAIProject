from ._processorParams import ProcessorParams
from ._dataRecorder import DataRecorder
from ._sharedData import SharedData
import random


class Processor:

  def __init__(self, sharedDataId=None, reverse=None, name: str = None):
    if sharedDataId == None:
      self.sharedDataId = random.random()
    else:
      self.sharedDataId = sharedDataId
    self.reverseProcessor = reverse
    self.name = name

  def scale(self, data, project, params: ProcessorParams = None):
    pass

  def apply(self, data, project, params: ProcessorParams = None):
    pass

  def reverse(self):
    if self.reverseProcessor == None:
      from ..processor._noneProcessor import NoneProcessor
      return NoneProcessor()
    return self.reverseProcessor

  def saveData(self, dataRecorder: DataRecorder) -> None:
    dataRecorder.recordBase(self)
    dataRecorder.record('name', self.name)
    if (self.reverseProcessor != None):
      self.reverseProcessor.saveData(
          dataRecorder.getChild('reverseProcessor')
      )

  def getSharedData(self, project) -> SharedData:
    return project.sharedData.getOrCreate(self.sharedDataId)
