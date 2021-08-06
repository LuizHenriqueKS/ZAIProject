from ZAIProject.base import Loader
from .._intToBinary import IntToBinary


class IntToBinaryProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == IntToBinary.__name__

  def load(self, loaders, project, data):
    return IntToBinary(
        self.tryGetData(data, 'binaryLength'),
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )
