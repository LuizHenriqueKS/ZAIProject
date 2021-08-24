from ZAIProject.base import Loader
from .._padding2D import Padding2D


class Padding2DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Padding2D.__name__

  def load(self, loaders, project, data):
    return Padding2D(
        leftLength=data['leftLength'],
        rightLength=data['rightLength'],
        value=data['value'],
        shape=self.tryGetData(data, 'shape'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
