from ..base._processor import Processor
from ..utility._convertIndexToClass import convertIndexToClass


class IndexToClass(Processor):

    def __init__(self, sharedDataId=None, reverse=None):
        super().__init__(sharedDataId=sharedDataId, reverse=reverse)

    def scale(self, data, project, params):
        self.updateLength(project, len(data))
        return self.apply(data, project, params)

    def apply(self, data, project, params):
        return convertIndexToClass(data, self.getLength(data))

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._classToIndex import ClassToIndex
        return ClassToIndex(sharedDataId=self.sharedDataId)

    def updateLength(self, project, length):
        currentLength = self.getLength(project)
        self.getSharedData(project)['length'] = max([length, currentLength])

    def getLength(self, project):
        sharedData = self.getSharedData(project)
        if not 'length' in sharedData:
            return 0
        return sharedData['length']
