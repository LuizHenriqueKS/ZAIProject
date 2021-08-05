from ..base import Processor
from ..utility import getShape
import numpy as np


class Reshape(Processor):

  def __init__(self, targetShape, sharedDataId=None, reverse=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)
    self.targetShape = targetShape

  def scale(self, data, project, params=None):
    self.updateShape(project, data)
    return self.apply(data)

  def apply(self, data, project, params=None):
    targetShape = self.targetShape
    if targetShape == None:
      targetShape = self.getSharedData(project)['targetShape']
    return np.array(data).reshape(targetShape)

  def reverse(self):
    raise NotImplementedError()

  def updateShape(self, project, data):
    shape = getShape(data)
    sharedData = self.getSharedData(project)
    if 'targetShape' not in sharedData:
      sharedData['targetShape'] = shape
    elif sharedData['targetShape'] != shape:
      raise ValueError(
          f'The shapes are differents: {shape} vs {sharedData["targetShape"]}'
      )
