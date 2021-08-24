from ZAIProject.base import Loader
from .._audioSamplesToMelspectrogram import AudioSamplesToMelspectrogram


class AudioSamplesToMelspectrogramProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == AudioSamplesToMelspectrogram.__name__

  def load(self, loaders, project, data):
    return AudioSamplesToMelspectrogram(
        sampleRate=data['sampleRate'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
