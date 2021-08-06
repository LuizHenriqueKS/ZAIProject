from ..base._processor import Processor


class BinaryToInt(Processor):

  def __init__(self, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.binaryLength = None

  def scale(self, data, project, params=None):
    self.updateBinaryLength(data)
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    strVector = [str(round(i)) for i in data]
    binaryStr = ''.join(strVector)
    result = int(binaryStr, 2)
    return result

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._intToBinary import IntToBinary
    return IntToBinary(sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('binaryLength', self.binaryLength)

  def getBinaryLength(self, project):
    if self.binaryLength != None:
      return self.binaryLength
    sharedData = self.getSharedData(project)
    if 'binaryLength' in sharedData:
      return sharedData['binaryLength']

  def updateBinaryLength(self, project, binaryLength):
    if self.binaryLength == None:
      currentBinaryLength = self.getBinaryLength(binaryLength)
      if currentBinaryLength == None or currentBinaryLength < binaryLength:
        self.getSharedData(project)['binaryLength'] = binaryLength
