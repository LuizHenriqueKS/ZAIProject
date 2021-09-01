from ZAIProject.base import Loader
from .._outputLength import OutputLength


class OutputLengthProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == OutputLength.__name__

  def load(self, loaders, project, data):
    return OutputLength(
        index=data['index'],
        returnSequence=data['returnSequence'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
