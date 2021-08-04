from ..base._dataApplier import DataApplier
from ..base._processorParams import ProcessorParams


class RecursiveDataApplier(DataApplier):

  def __init__(self, project, parentApplier, recursive):
    super().__init__()
    self.project = project
    self.parentApplier = parentApplier
    self.recursive = recursive
    self.maxNumTargets = 0

  def iterScaleFitInputOne(self, one):
    return self.iterApplyInputOne(one, mode="scale")

  def iterApplyFitInputOne(self, data):
    return self.iterApplyInputOne(data, mode="fit")

  def iterScaleFitTargetOne(self, one):
    return self.splitIterTarget(self.parentApplier.iterScaleFitTargetOne(one))

  def iterApplyFitTargetOne(self, one):
    return self.splitIterTarget(self.parentApplier.iterApplyFitTargetOne(one))

  def iterApplyPredictInputOne(self, one):
    return self.parentApplier.iterApplyPredictInputOne(one)

  def iterApplyPredictTargetOne(self, one):
    return self.parentApplier.iterApplyPredictTargetOne(one)

  def iterApplyPredictOutputOne(self, one):
    return self.parentApplier.iterApplyPredictOutputOne(one)

  def runPredict(self, dataApplier, predictFunc, data, context):
    outputs = []
    for one in data:
      params = ProcessorParams(
          mode='predict',
          io="input",
          contextIteration=0,
          context=[[]]
      )
      while self.canContinuePredict(params):
        input = dataApplier.predict(one, params)
        modelOutput = predictFunc([input])[0]
        context = self.recursive.convertOutputToContext(modelOutput)
        self.updateContext(params, context)
      output = self.recursive.getOutput(params)
      outputs.append(output)
    return self.applyPredictOutput(outputs)

  def canContinuePredict(self, params):
    return len(params.context[0]) < self.maxNumTargets

  def splitIterTarget(self, iterTarget):
    fullTarget = next(iterTarget)
    return self.recursive.splitTarget(fullTarget)

  def iterApplyInputOne(self, one, mode):
    params = ProcessorParams(
        mode=mode,
        io="input",
        contextIteration=0,
        context=[]
    )
    input = self.projectApplyInputOne(mode, one, params)
    yield input
    targets = self.applyTargetOne(mode, one)
    self.maxNumTargets = max(self.maxNumTargets, len(targets) - 1)
    for i in range(0, len(targets) - 1):
      target = targets[i]
      self.updateContext(params, target)
      input = self.projectApplyInputOne(mode, one, params)
      yield input

  def updateContext(self, params, target):
    for io in range(0, len(target)):
      if len(params.context) <= io:
        params.context.append([])
      params.context[io].append(target[io])
    params.contextIteration += 1

  def projectApplyInputOne(self, mode, one, params):
    if mode == 'fit':
      return self.project.fit.input.applyOne(one, params)
    elif mode == 'scale':
      return self.project.fit.input.scaleOne(one, params)
    else:
      raise NotImplementedError()

  def applyTargetOne(self, mode, one):
    if mode == 'fit':
      return self.applyFitTargetOne(one)
    elif mode == 'scale':
      return self.scaleFitTargetOne(one)
    else:
      raise NotImplementedError()
