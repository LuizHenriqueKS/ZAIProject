from ZAIProject.base import Loader
from .._trim1D import Trim1D


class Trim1DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Trim1D.__name__

  def load(self, loaders, project, data):
    return Trim1D(
        direction=self.tryGetData(data, 'direction'),
        value=self.tryGetData(data, 'value'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
