from ZAIProject.base import Loader
from .._downQualityAudioSamples import DownQualityAudioSamples


class DownQualityAudioSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == DownQualityAudioSamples.__name__

  def load(self, loaders, project, data):
    return DownQualityAudioSamples(
        bits=data['bits'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
