from ZAIProject.base import Loader
from .._indexToValue import IndexToValue


class IndexToValueProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == IndexToValue.__name__

  def load(self, loaders, project, data):
    return IndexToValue(
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )