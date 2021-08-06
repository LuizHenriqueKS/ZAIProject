from ZAIProject.base import Loader
from .._sparse import Sparse


class SparseRecursiveLoader(Loader):

  def type(self):
    return 'recursive'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Sparse.__name__

  def load(self, loaders, project, data):
    result = Sparse(
        data['contextShape'],
        data['maxLengthContext']
    )
    result.emptyValue = data['emptyValue']
    return result
