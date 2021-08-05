from ZAIProject.base import Loader
from .._custom import Custom


class CustomRecursiveLoader(Loader):

  def type(self):
    return 'recursive'

  def canLoad(self, loaders, project, data) -> bool:
    return data['type'] == Custom.__name__

  def load(self, loaders, project, data):
    return Custom(
        loaders.load('processor', project, data['processor']),
        data['contextShape'],
        data['maxLengthContext']
    )
