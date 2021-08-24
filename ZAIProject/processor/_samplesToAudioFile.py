from random import sample

from numpy import lib
from ..base._processor import Processor
from ..validation import requireStr
import soundfile
import tempfile


class SamplesToAudioFile(Processor):

  def __init__(self, sampleRate, dtype='float32', sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.sampleRate = sampleRate
    self.dtype = dtype

  def scale(self, data, project=None, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    file = tempfile.TemporaryFile(suffix='.wav').name
    soundfile.write(file, data, self.sampleRate)
    return file

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._audioFileToSamples import AudioFileToSamples
    return AudioFileToSamples(sampleRate=self.sampleRate, dtype=self.dtype, sharedDataId=self.sharedDataId)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('sampleRate', self.sampleRate)
    dataRecorder.record('dtype', self.dtype)
