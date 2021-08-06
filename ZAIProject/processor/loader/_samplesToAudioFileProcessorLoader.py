from ZAIProject.base import Loader
from .._samplesToAudioFile import SamplesToAudioFile


class SamplesToAudioFileProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == SamplesToAudioFile.__name__

  def load(self, loaders, project, data):
    return SamplesToAudioFile(
        sampleRate=data['sampleRate'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
