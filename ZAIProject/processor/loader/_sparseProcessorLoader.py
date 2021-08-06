from ZAIProject.base import Loader
from .._sparse import Sparse


class SparseProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Sparse.__name__

  def load(self, loaders, project, data):
    return Sparse(
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor')
    )
