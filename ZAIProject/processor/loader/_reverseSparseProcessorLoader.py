from ZAIProject.base import Loader
from .._reverseSparse import ReverseSparse


class ReverseSparseProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ReverseSparse.__name__

  def load(self, loaders, project, data):
    return ReverseSparse(
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
