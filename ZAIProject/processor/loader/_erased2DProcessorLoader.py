from ZAIProject.base import Loader
from .._eraser2D import Eraser2D


class Erased2DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Eraser2D.__name__

  def load(self, loaders, project, data):
    return Eraser2D(
        direction=data['direction'],
        value=data['value'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
