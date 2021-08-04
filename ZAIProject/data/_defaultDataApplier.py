from ..base._dataApplier import DataApplier
from ..base._processorParams import ProcessorParams


class DefaultDataApplier(DataApplier):

  def __init__(self, project) -> None:
    super().__init__()
    self.project = project

  def iterScaleFitInputOne(self, one):
    params = ProcessorParams(mode='scale', io='input')
    yield self.project.fit.input.scaleOne(one, params)

  def iterScaleFitTargetOne(self, one):
    params = ProcessorParams(mode='scale', io='target')
    yield self.project.fit.output.scaleOne(one, params)

  def iterApplyFitInputOne(self, one):
    params = ProcessorParams(mode='fit', io='input')
    yield self.project.fit.input.applyOne(one, params)

  def iterApplyFitTargetOne(self, one):
    params = ProcessorParams(mode='fit', io='target')
    yield self.project.fit.output.applyOne(one, params)

  def iterApplyPredictInputOne(self, one):
    params = ProcessorParams(mode='predict', io='input')
    yield self.project.predict.input.applyOne(one, params)

  def iterApplyPredictTargetOne(self, one):
    params = ProcessorParams(mode='predict', io='target')
    yield self.project.predict.output.applyOnePerIO(one, params)

  def iterApplyPredictOutputOne(self, one):
    params = ProcessorParams(mode='predict', io='output')
    result = self.project.predict.output.applyOnePerIO(one, params)
    yield result

  def runPredict(self, predictFunc, data, context):
    modelInput = self.applyPredictInput(data)
    modelOutput = predictFunc(modelInput)
    output = self.applyPredictOutput(modelOutput)
    return output

  def runEvaluate(self, predictFunc, data, table):
    input = self.applyFitInput(data)
    target = self.applyFitTarget(data)
    predictTarget = None
    predictOutput = None
    if table:
      predictTarget = self.applyPredictTarget(target)
      modelOutput = predictFunc(input)
      predictOutput = self.applyPredictOutput(modelOutput)
    return (input, target, predictTarget, predictOutput)
