from ZAIProject.base import Loader
from .._context import Context


class ContextProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return data['type'] == Context.__name__

  def load(self, loaders, project, data):
    return Context(
        data['contextIndex'],
        data['returnSequences'],
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor')
    )
