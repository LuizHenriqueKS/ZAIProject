from tensorflow._api.v2 import data


class IOInfo:
  def __init__(self):
    self.shape = None
    self.minValue = None
    self.maxValue = None

  def saveData(self, dataRecorder):
    dataRecorder.record('shape', self.shape)
    dataRecorder.record('minValue', self.minValue)
    dataRecorder.record('maxValue', self.maxValue)
