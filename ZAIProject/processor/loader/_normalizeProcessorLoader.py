from ZAIProject.base import Loader
from .._normalize import Normalize


class NormalizeProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Normalize.__name__

  def load(self, loaders, project, data):
    return Normalize(
        minOutput=self.tryGetData(data, 'minOutput'),
        maxOutput=self.tryGetData(data, 'maxOutput'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
