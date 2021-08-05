from ZAIProject.base import Loader
from .._slice1D import Slice1D


class Slice1DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return data['type'] == Slice1D.__name__

  def load(self, loaders, project, data):
    return Slice1D(
        data['start'],
        data['end'],
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor')
    )
