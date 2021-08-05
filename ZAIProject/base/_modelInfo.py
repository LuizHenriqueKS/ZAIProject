from tensorflow._api.v2 import data
from ._ioInfo import IOInfo
from typing import List


class ModelInfo:
  def __init__(self):
    self.input: List[IOInfo] = []
    self.output: List[IOInfo] = []
    pass

  def saveData(self, dataRecorder):
    dataRecorder.record('type', ModelInfo.__name__)
    for i in range(0, len(self.input)):
      self.input[i].saveData(dataRecorder.getChild(f'input{i:05d}'))
    for i in range(0, len(self.output)):
      self.output[i].saveData(dataRecorder.getChild(f'output{i:05d}'))
