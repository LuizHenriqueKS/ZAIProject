from numpy.core.fromnumeric import transpose
from ..base._processor import Processor
from ..utility import applyRuleOf3
import numpy as np
import librosa
import numpy as np


class SpectrogramToAudioSamples(Processor):

  def __init__(self, returnMagnitude=True, returnPhase=True, transpose=True, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.transpose = transpose
    self.returnMagnitude = returnMagnitude
    self.returnPhase = returnPhase

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    result = np.array(data, dtype=np.float)
    if self.returnMagnitude and self.returnPhase:
      result = result[0] * np.exp(1j * result[1])
    if self.transpose:
      result = result.transpose()
    return librosa.istft(result)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('transpose', self.transpose)
    dataRecorder.record('returnMagnitude', self.returnMagnitude)
    dataRecorder.record('returnPhase', self.returnPhase)

  def reverse(self):
    if self.reverseProcessor != None:
      return super().reverse()
    else:
      from ._audioSamplesToSpectrogram import AudioSamplesToSpectrogram
      return AudioSamplesToSpectrogram(returnMagnitude=self.returnMagnitude, returnPhase=self.returnPhase, transpose=self.transpose, sharedDataId=self.sharedDataId)
