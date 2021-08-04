from ._projectFit import ProjectFit
from ._projectPredict import ProjectPredict
from ._modelInfo import ModelInfo
from ..utility._getShape import getShape
from ..utility._getMaxShape import getMaxShape
from ..utility._getMinValue import getMinValue
from ..utility._getMaxValue import getMaxValue
from ..base._ioInfo import IOInfo
from ._sharedData import SharedData
from ..data._defaultDataApplier import DefaultDataApplier
from ..data._recursiveDataApplier import RecursiveDataApplier


class Project:

  def __init__(self, recursive=None):
    self.fit = ProjectFit(self)
    self.predict = ProjectPredict(self)
    self.modelInfo = ModelInfo()
    self.sharedData = SharedData()
    self._dataApplier = DefaultDataApplier(self)
    if recursive != None:
      self._dataApplier = RecursiveDataApplier(
          self,
          self._dataApplier,
          recursive
      )

  def scale(self, data, verbose: bool = False):
    maxProgress = len(data)
    currentProgress = 0
    for one in data:
      for input in self.dataApplier().iterScaleFitInputOne(one):
        for j in range(0, len(input)):
          self.updateIOInfo(j, self.modelInfo.input, input)
      for output in self.dataApplier().iterScaleFitTargetOne(one):
        for j in range(0, len(output)):
          self.updateIOInfo(j, self.modelInfo.output, output)
      currentProgress += 1
      if (verbose):
        print(f'{currentProgress}/{maxProgress} Scaling...')

  def updateIOInfo(self, index, ioInfo, data):
    if len(ioInfo) <= index:
      ioInfo.append(IOInfo())
    if len(data[index]) > 0:
      ioInfo[index].shape = getMaxShape(
          getShape(data[index]),
          ioInfo[index].shape
      )
      ioInfo[index].minValue = self.myMin(
          getMinValue(data[index]),
          ioInfo[index].minValue
      )
      ioInfo[index].maxValue = self.myMax(
          getMaxValue(data[index]),
          ioInfo[index].maxValue
      )

  def myMin(self, a, b):
    if b == None:
      return a
    return min([a, b])

  def myMax(self, a, b):
    if b == None:
      return a
    return max([a, b])

  def dataApplier(self):
    return self._dataApplier
