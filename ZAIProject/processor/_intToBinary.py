from ZAIProject import data
from ..base._processor import Processor


class IntToBinary(Processor):

  def __init__(self, binaryLength=None, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.binaryLength = binaryLength

  def scale(self, data, project, params=None):
    binary = self.apply(data, project, params, ignoreLength=True)
    self.updateBinaryLength(project, len(binary))
    return binary

  def apply(self, data, project, params=None, ignoreLength=False):
    length = self.getBinaryLength(project)
    binary = [int(x) for x in list('{0:0b}'.format(data))]
    if length != None:
      while length > len(binary):
        binary.insert(0, 0)
      if not ignoreLength:
        assert len(
            binary) <= length, "binary.length > maxLength, binary={binary} length={length}"
    return binary

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._binaryToInt import BinaryToInt
    return BinaryToInt(sharedDataId=self.sharedDataId)

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
      currentBinaryLength = self.getBinaryLength(project)
      if currentBinaryLength == None or currentBinaryLength < binaryLength:
        self.getSharedData(project)['binaryLength'] = binaryLength
