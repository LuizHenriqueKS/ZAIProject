from ZAIProject.base import Loader
from .._eraser1D import Eraser1D


class Erased1DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Eraser1D.__name__

  def load(self, loaders, project, data):
    return Eraser1D(
        data['direction'],
        data['value'],
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor')
    )
