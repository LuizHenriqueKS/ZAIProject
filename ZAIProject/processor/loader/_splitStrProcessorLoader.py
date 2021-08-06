from ZAIProject.base import Loader
from .._splitStr import SplitStr


class SplitStrProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == SplitStr.__name__

  def load(self, loaders, project, data):
    return SplitStr(
        separator=data['separator'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
