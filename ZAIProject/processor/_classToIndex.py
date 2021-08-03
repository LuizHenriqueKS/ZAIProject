from ..base._processor import Processor
from ..utility._getBestIndex import getBestIndex
from ..validation._requireFloatArray import requireFloatArray


class ClassToIndex(Processor):

    def __init__(self, sharedDataId=None, reverse=None):
        super().__init__(sharedDataId=sharedDataId, reverse=reverse)

    def scale(self, data, project, params):
        return self.apply(data, project, params)

    def apply(self, data, project, params):
        requireFloatArray(data)
        return getBestIndex(data)

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._indexToClass import IndexToClass
        return IndexToClass(sharedDataId=self.sharedDataId)
