from ZAIProject.base import Loader
from .._melspectrogramToAudioSamples import MelspectrogramToAudioSamples


class MelspectrogramToAudioSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == MelspectrogramToAudioSamples.__name__

  def load(self, loaders, project, data):
    return MelspectrogramToAudioSamples(
        sampleRate=data['sampleRate'],
        transpose=data['transpose'],
        n_fft=self.tryGetData(data, 'n_fft', 2056),
        hop_length=self.tryGetData(data, 'hop_length', 512),
        n_mels=data['n_mels'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
