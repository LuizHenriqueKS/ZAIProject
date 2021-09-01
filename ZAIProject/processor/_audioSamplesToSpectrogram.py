from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa


class AudioSamplesToSpectrogram(Processor):

  def __init__(self, returnMagnitude=True, returnPhase=True, transpose=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.transpose = transpose
    self.returnMagnitude = returnMagnitude
    self.returnPhase = returnPhase

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    result = np.array(data)
    result = librosa.stft(result)
    if self.transpose:
      result = result.transpose()
    magnitude = np.abs(result)
    phase = np.angle(result)
    if self.returnPhase and self.returnMagnitude:
      return [magnitude, phase]
    elif self.returnMagnitude:
      return magnitude
    elif self.returnPhase:
      return phase

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('transpose', self.transpose)
    dataRecorder.record('returnMagnitude', self.returnMagnitude)
    dataRecorder.record('returnPhase', self.returnPhase)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._spectrogramToAudioSamples import SpectrogramToAudioSamples
      return SpectrogramToAudioSamples(returnMagnitude=self.returnMagnitude, returnPhase=self.returnPhase, transpose=self.transpose, sharedDataId=self.sharedDataId)
