from ZAIProject.base import Loader
from .._reverseNormalize import ReverseNormalize


class ReverseNormalizeLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ReverseNormalize.__name__

  def load(self, loaders, project, data):
    return ReverseNormalize(
        minOutput=data['minOutput'],
        maxOutput=data['maxOutput'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name')
    )
