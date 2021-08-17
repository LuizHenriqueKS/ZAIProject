from ZAIProject.base import Loader
from .._round import Round


class RoundProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Round.__name__

  def load(self, loaders, project, data):
    return Round(
        numOfDecimals=self.tryGetData(data, 'numOfDecimals'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
