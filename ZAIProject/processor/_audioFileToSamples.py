from random import sample

from ..base._processor import Processor
from ..validation import requireStr
import librosa
import soundfile


class AudioFileToSamples(Processor):

  def __init__(self, sampleRate, mono=False, dtype='float32', sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.mono = mono
    self.dtype = dtype
    self.sampleRate = sampleRate

  def scale(self, data, project=None, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    requireStr(data)
    samples, frameRate = librosa.load(
        data, mono=self.mono, sr=self.sampleRate, dtype=self.dtype)
    return samples

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('sampleRate', self.sampleRate)
    dataRecorder.record('mono', self.mono)
    dataRecorder.record('dtype', self.dtype)

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._samplesToAudioFile import SamplesToAudioFile
    return SamplesToAudioFile(sampleRate=self.sampleRate, dtype=self.dtype, sharedDataId=self.sharedDataId)
