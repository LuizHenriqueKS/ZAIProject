from ZAIProject.base import Loader
from .._noneProcessor import NoneProcessor


class NoneProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == NoneProcessor.__name__

  def load(self, loaders, project, data):
    return NoneProcessor(
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
