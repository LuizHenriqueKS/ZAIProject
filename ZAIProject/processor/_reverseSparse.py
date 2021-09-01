from ..base._processor import Processor
from tensorflow import argmax
import numpy as np


class ReverseSparse(Processor):

  def __init__(self, sharedDataId=None, reverse=None, name: str = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)

  def scale(self, data, project, params):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    data = np.array(data)
    if data.dtype == np.int:
      return data
    shape = data.shape
    result = argmax(data, len(shape) - 1)
    return result.numpy()

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._sparse import Sparse
    return Sparse()
