from ZAIProject.base import Loader
from .._valueToIndex import ValueToIndex


class ValueToIndexProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ValueToIndex.__name__

  def load(self, loaders, project, data):
    return ValueToIndex(
        unknownValue=self.tryGetData(data, 'unknownValue'),
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
