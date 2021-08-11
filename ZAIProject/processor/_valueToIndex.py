from ..base._processor import Processor


class ValueToIndex(Processor):
  def __init__(self, unknownValue='unknown', sharedDataId=None, reverse=None, name=None):
    super().__init__(reverse=reverse, sharedDataId=sharedDataId, name=name)
    self.unknownValue = unknownValue
    self.reverseDict = {}

  def scale(self, data, project, params=None):
    try:
      return self.getReverseDict(project)[f'{data}']
    except KeyError:
      dict = self.getDict(project)
      reverseDict = self.getReverseDict(project)
      index = len(dict)
      reverseDict[f'{data}'] = index
      dict.append(data)
      return index

  def apply(self, data, project, params=None):
    try:
      return self.getReverseDict(project)[f'{data}']
    except:
      index = 0
    return index

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._indexToValue import IndexToValue
    return IndexToValue(self.sharedDataId)

  def getDict(self, project):
    sharedData = self.getSharedData(project)
    if not 'dict' in sharedData:
      dict = [self.unknownValue]
      sharedData['dict'] = dict
    return sharedData['dict']

  def getReverseDict(self, project):
    sharedData = self.getSharedData(project)
    if not 'reverseDict' in sharedData:
      reverseDict = {}
      reverseDict[f'{self.unknownValue}'] = 0
      sharedData['reverseDict'] = reverseDict
    return sharedData['reverseDict']

  def setDict(self, project, dict):
    sharedData = self.getSharedData(project)
    sharedData['dict'] = dict
    sharedData['unknownValue'] = self.unknownValue
    return self
