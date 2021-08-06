from ZAIProject.base import Loader
from .._audioFileToSamples import AudioFileToSamples


class AudioFileToSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == AudioFileToSamples.__name__

  def load(self, loaders, project, data):
    return AudioFileToSamples(
        data['sampleRate'],
        data['mono'],
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )
