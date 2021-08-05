from ..base._processor import Processor
import numpy as np
from ..utility import getShape


class Flatten(Processor):

  def __init__(self, sharedDataId=None, reverse=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)

  def scale(self, data, project, params=None):
    self.updateShape(project, data)
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    return np.array(data).flatten()

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._reshape import Reshape
    return Reshape(sharedDataId=self.sharedDataId)

  def updateShape(self, project, data):
    shape = getShape(data)
    sharedData = self.getSharedData(project)
    if 'targetShape' not in sharedData:
      sharedData['targetShape'] = shape
    elif sharedData['targetShape'] != shape:
      raise ValueError(
          f'The shapes are differents: {shape} vs {sharedData["targetShape"]}'
      )
