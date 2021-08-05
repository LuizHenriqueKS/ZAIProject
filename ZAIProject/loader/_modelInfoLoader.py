from ..base._modelInfo import ModelInfo
from ..base._ioInfo import IOInfo
from ..base._loader import Loader


class ModelInfoLoader(Loader):

  def type(self):
    return 'modelInfo'

  def canLoad(self, loaders, project, data) -> bool:
    return data['type'] == ModelInfo.__name__

  def load(self, loaders, project, data):
    modelInfo = ModelInfo()
    for key in data.keys():
      if key.startswith('input'):
        set = modelInfo.input
      elif key.startswith('output'):
        set = modelInfo.output
      else:
        set = None
      if set != None:
        ioInfo = IOInfo()
        ioInfo.shape = tryGet(data[key], 'shape')
        ioInfo.minValue = tryGet(data[key], 'minValue')
        ioInfo.maxValue = tryGet(data[key], 'maxValue')
        set.append(ioInfo)
    return modelInfo


def tryGet(data, key):
  if key in data:
    return data[key]
  return None
