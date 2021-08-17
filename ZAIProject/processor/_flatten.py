from ..base._processor import Processor
import numpy as np
from ..utility import getShape, getMaxShape


class Flatten(Processor):

  def __init__(self, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)

  def scale(self, data, project, params=None):
    self.updateShape(project, data)
    return self.flatten(data)

  def apply(self, data, project=None, params=None):
    return np.array(data).flatten()

  def flatten(self, data):
    if isinstance(data, list):
      result = []
      for one in data:
        for i in self.flatten(one):
          result.append(i)
      return result
    return [data]

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._reshape import Reshape
    return Reshape(sharedDataId=self.sharedDataId)

  def updateShape(self, project, data):
    shape = getShape(data)
    sharedData = self.getSharedData(project)
    if 'targetShape' not in sharedData or sharedData['targetShape'] == 0:
      sharedData['targetShape'] = shape
    elif sharedData['targetShape'] != shape and shape != 0:
      shape = getMaxShape(shape, sharedData['targetShape'])
      sharedData['targetShape'] = shape
      '''raise ValueError(
          f'The shapes are differents: {shape} vs {sharedData["targetShape"]}'
      )'''
