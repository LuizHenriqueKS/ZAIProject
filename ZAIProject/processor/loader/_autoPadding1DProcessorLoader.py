from ZAIProject.base import Loader
from .._autoPadding1D import AutoPadding1D


class AutoPadding1DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == AutoPadding1D.__name__

  def load(self, loaders, project, data):
    return AutoPadding1D(
        direction=data['direction'],
        value=data['value'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
