from ZAIProject.base import Loader
from .._autoPadding2D import AutoPadding2D


class AutoPadding2DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == AutoPadding2D.__name__

  def load(self, loaders, project, data):
    return AutoPadding2D(
        direction=data['direction'],
        value=data['value'],
        shape=self.tryGetData(data, 'shape'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
