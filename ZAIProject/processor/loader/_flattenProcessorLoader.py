from ZAIProject.base import Loader
from .._flatten import Flatten


class FlattenProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Flatten.__name__

  def load(self, loaders, project, data):
    return Flatten(
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )
