from ..base._processor import Processor
import inspect


class Lambda(Processor):

  def __init__(self, lambdaFunc, lambdaExpression=None, recordable=True, sharedDataId=None, reverse=None, name=None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse, name=name)
    self.lambdaFunc = lambdaFunc
    self.recordable = recordable
    self.lambdaExpression = lambdaExpression
    self.lambdaParamsNum = str(
        inspect.signature(self.lambdaFunc)
    ).count(",") + 1

  def scale(self, data, project, params):
    return self.apply(data, project, params)

  def apply(self, data, project, params):
    if self.lambdaParamsNum == 1:
      return self.lambdaFunc(data)
    elif self.lambdaParamsNum == 2:
      return self.lambdaFunc(data, project)
    return self.lambdaFunc(data, project, params)

  def saveData(self, dataRecorder) -> None:
    super().saveData(dataRecorder)
    if self.recordable:
      lambdaFunc = self.lambdaExpression
      if lambdaFunc is None:
        lambdaFunc = inspect.getsourcelines(self.lambdaFunc)
      dataRecorder.record('lambdaFunc', lambdaFunc)
