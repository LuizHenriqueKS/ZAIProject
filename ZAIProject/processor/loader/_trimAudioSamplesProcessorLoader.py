from ZAIProject.base import Loader
from .._trimAudioSamples import TrimAudioSamples


class TrimAudioSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == TrimAudioSamples.__name__

  def load(self, loaders, project, data):
    return TrimAudioSamples(
        bits=data['bits'],
        distance=data['distance'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
