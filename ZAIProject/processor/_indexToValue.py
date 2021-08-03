from ..base._processor import Processor
from ..validation._requireInt import requireInt
from ..validation._requireFloatArray import requireFloatArray
from ..utility._getBestIndex import getBestIndex


class IndexToValue(Processor):
    def __init__(self, sharedDataId=None, reverse=None):
        super().__init__(reverse=reverse)
        if sharedDataId != None:
            self.sharedDataId = sharedDataId

    def scale(self, data, project, params=None):
        raise NotImplementedError()

    def apply(self, data, project, params=None):
        dict = self.getDict(project)
        if isinstance(data, list):
            requireFloatArray(data)
            data = getBestIndex(data)
        requireInt(data)
        index = dict[data]
        return index

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._valueToIndex import ValueToIndex
        return ValueToIndex(sharedDataId=self.sharedDataId)

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
