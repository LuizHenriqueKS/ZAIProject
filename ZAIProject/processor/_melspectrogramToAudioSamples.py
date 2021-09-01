from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa


class MelspectrogramToAudioSamples(Processor):

  def __init__(self, sampleRate, n_mels=128, transpose=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.sampleRate = sampleRate
    self.transpose = transpose
    self.n_mels = n_mels

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    result = np.array(data, dtype=np.float)
    if self.transpose:
      result = result.transpose()
    return librosa.feature.inverse.mel_to_audio(result, sr=self.sampleRate)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('sampleRate', self.sampleRate)
    dataRecorder.record('transpose', self.transpose)
    dataRecorder.record('n_mels', self.n_mels)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._audioSamplesToMelspectrogram import AudioSamplesToMelspectrogram
      return AudioSamplesToMelspectrogram(sampleRate=self.sampleRate, sharedDataId=self.sharedDataId, n_mels=self.n_mels)
