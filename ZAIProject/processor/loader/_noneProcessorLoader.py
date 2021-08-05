from ZAIProject.base import Loader
from .._noneProcessor import NoneProcessor


class NoneProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return data['type'] == NoneProcessor.__name__

  def load(self, loaders, project, data):
    return NoneProcessor(
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor')
    )
