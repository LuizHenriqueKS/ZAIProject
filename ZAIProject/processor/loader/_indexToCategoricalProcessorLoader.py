from ZAIProject.base import Loader
from .._indexToCategorical import IndexToCategorical


class IndexToCategoricalProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == IndexToCategorical.__name__

  def load(self, loaders, project, data):
    return IndexToCategorical(
        length=self.tryGetData(data, 'length'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
