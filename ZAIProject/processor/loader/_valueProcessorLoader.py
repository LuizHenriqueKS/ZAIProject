from ZAIProject.base import Loader
from .._value import Value


class ValueProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Value.__name__

  def load(self, loaders, project, data):
    return Value(
        value=self.tryGetData(data, 'value'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
