from ZAIProject.base import Loader
from .._treatRepetitions import TreatRepetitions


class TreatRepetitionsProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == TreatRepetitions.__name__

  def load(self, loaders, project, data):
    return TreatRepetitions(
        returnSequence=data['returnSequence'],
        returnRepetitions=data['returnRepetitions'],
        endValue=data['endValue'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
