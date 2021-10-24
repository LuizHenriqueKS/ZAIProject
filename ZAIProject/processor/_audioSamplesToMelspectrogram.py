from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa


class AudioSamplesToMelspectrogram(Processor):

  def __init__(self, sampleRate, n_fft=2048, hop_length=512, n_mels=128, transpose=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.sampleRate = sampleRate
    self.transpose = transpose
    self.n_mels = n_mels
    self.n_fft = n_fft
    self.hop_length = hop_length

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    result = np.array(data)
    result = librosa.feature.melspectrogram(
        result, sr=self.sampleRate, n_mels=self.n_mels, n_fft=self.n_fft, hop_length=self.hop_length)
    if self.transpose:
      result = result.transpose()
    return result

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('sampleRate', self.sampleRate)
    dataRecorder.record('transpose', self.transpose)
    dataRecorder.record('n_mels', self.n_mels)
    dataRecorder.record('n_fft', self.n_fft)
    dataRecorder.record('hop_length', self.hop_length)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._melspectrogramToAudioSamples import MelspectrogramToAudioSamples
      return MelspectrogramToAudioSamples(sampleRate=self.sampleRate, n_mels=self.n_mels, n_fft=self.n_fft, hop_length=self.hop_length, transpose=self.transpose, sharedDataId=self.sharedDataId)
