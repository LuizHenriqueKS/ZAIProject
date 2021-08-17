from logging import exception
from ..base._processor import Processor
from typing import Literal


class Value(Processor):

  def __init__(self, value=None, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.value = value

  def scale(self, data, project, params=None):
    return self.apply(data, project, params)

  def apply(self, data, project, params=None):
    return self.value

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    dataRecorder.record('value', self.value)
