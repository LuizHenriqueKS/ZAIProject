from ZAIProject.base import Loader
from .._binaryToInt import BinaryToInt


class BinaryToIntProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == BinaryToInt.__name__

  def load(self, loaders, project, data):
    return BinaryToInt(
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
