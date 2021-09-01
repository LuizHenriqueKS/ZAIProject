from ZAIProject.base import Loader
from .._reverseTreatRepetitions import ReverseTreatRepetitions


class ReverseTreatRepetitionsProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ReverseTreatRepetitions.__name__

  def load(self, loaders, project, data):
    return ReverseTreatRepetitions(
        returnSequence=data['returnSequence'],
        returnRepetitions=data['returnRepetitions'],
        endValue=data['endValue'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
