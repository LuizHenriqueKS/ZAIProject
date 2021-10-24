from ZAIProject.base import Loader
from .._spectrogramToAudioSamples import SpectrogramToAudioSamples


class SpectrogramToAudioSamplesProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == SpectrogramToAudioSamples.__name__

  def load(self, loaders, project, data):
    return SpectrogramToAudioSamples(
        returnMagnitude=data['returnMagnitude'],
        returnPhase=data['returnPhase'],
        transpose=data['transpose'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
