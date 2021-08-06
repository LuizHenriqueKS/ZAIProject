from ZAIProject.base import Loader
from .._context import Context


class ContextProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Context.__name__

  def load(self, loaders, project, data):
    return Context(
        contextIndex=data['contextIndex'],
        returnSequences=data['returnSequences'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
