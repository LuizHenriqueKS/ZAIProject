from ZAIProject.base import Loader
from .._splitStr import SplitStr


class SplitStrProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == SplitStr.__name__

  def load(self, loaders, project, data):
    return SplitStr(
        data['separator'],
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )
