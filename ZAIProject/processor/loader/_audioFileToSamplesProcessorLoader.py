from ZAIProject.base import Loader
from .._audioFileToSamples import AudioFileToSamples


class AudioFileToSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == AudioFileToSamples.__name__

  def load(self, loaders, project, data):
    return AudioFileToSamples(
        sampleRate=data['sampleRate'],
        mono=data['mono'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
