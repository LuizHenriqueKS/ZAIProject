from random import sample

from numpy import lib
from ..base._processor import Processor
from ..validation import requireStr
import librosa


class AudioFileToSamples(Processor):

  def __init__(self, sampleRate=None, mono=False, sharedDataId=None, reverse=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)
    self.sampleRate = sampleRate
    self.mono = mono

  def scale(self, data, project=None, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    requireStr(data)
    samples, frameRate = librosa.load(data, mono=self.mono, sr=self.sampleRate)
    return samples

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('sampleRate', self.sampleRate)
    dataRecorder.record('mono', self.mono)
