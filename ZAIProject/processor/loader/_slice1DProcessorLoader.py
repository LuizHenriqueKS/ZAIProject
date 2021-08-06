from ZAIProject.base import Loader
from .._slice1D import Slice1D


class Slice1DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Slice1D.__name__

  def load(self, loaders, project, data):
    return Slice1D(
        start=data['start'],
        end=data['end'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
