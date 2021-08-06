from ZAIProject.base import Loader
from .._intToBinary import IntToBinary


class IntToBinaryProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == IntToBinary.__name__

  def load(self, loaders, project, data):
    return IntToBinary(
        binaryLength=self.tryGetData(data, 'binaryLength'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
