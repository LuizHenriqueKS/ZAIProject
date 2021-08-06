from ZAIProject.base import Loader
from .._contextLength import ContextLength


class ContextLengthProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ContextLength.__name__

  def load(self, loaders, project, data):
    return ContextLength(
        contextIndex=data['contextIndex'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
