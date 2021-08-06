from ..base._processor import Processor


class ValueToIndex(Processor):
  def __init__(self, sharedDataId=None, reverse=None, name=None):
    super().__init__(reverse=reverse, sharedDataId=sharedDataId, name=name)

  def scale(self, data, project, params=None):
    dict = self.getDict(project)
    if not data in dict:
      dict.append(data)
      self.setDict(project, dict)
    return dict.index(data)

  def apply(self, data, project, params=None):
    try:
      dict = self.getDict(project)
      index = dict.index(data)
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
      dict = ['<unkown>']
      sharedData['dict'] = dict
    return sharedData['dict']

  def setDict(self, project, dict):
    sharedData = self.getSharedData(project)
    sharedData['dict'] = dict
    return self
