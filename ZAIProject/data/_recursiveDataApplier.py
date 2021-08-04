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

  def runPredict(self, predictFunc, data, context):
    contextIter = iter(context)
    for one in data:
      preOneContext = next(contextIter)
      if preOneContext == None:
        oneContext = None
      else:
        preOneContext2 = self.project.predict.context.applyOne(preOneContext)
        oneContext = list(self.recursive.splitTarget(preOneContext2))
      yield self.runPredictOne(predictFunc, one, oneContext, 'predict')

  def runPredictOne(self, predictFunc, one, context, mode):
    if context == None:
      context = []
    params = ProcessorParams(
        mode=mode,
        io="input",
        contextIteration=0,
        context=context
    )
    while self.canContinuePredict(params):
      if mode == 'predict':
        input = self.project.predict.input.applyOne(one, params)
      elif mode == 'fit':
        input = self.project.fit.input.applyOne(one, params)
      else:
        raise ValueError()
      modelOutput = predictFunc([input])[0]
      context = self.recursive.convertOutputToContext(modelOutput)
      self.updateContext(params, context)
    output = self.recursive.getOutput(params)
    return self.parentApplier.applyPredictOutputOne(output)[0]

  def runEvaluate(self, predictFunc, data, table):
    input = self.applyFitInput(data)
    target = self.applyFitTarget(data)
    predictTarget = None
    predictOutput = None
    if table:
      parentTarget = self.parentApplier.applyFitTarget(data)
      predictTarget = self.parentApplier.applyPredictTarget(parentTarget)
      predictOutput = []
      for one in data:
        oneOutput = self.runPredictOne(
            predictFunc,
            one,
            context=None,
            mode='fit'
        )
        predictOutput.append(oneOutput)
    return (input, target, predictTarget, predictOutput)

  def canContinuePredict(self, params):
    length = len(params.context)
    if length > 0:
      length = len(params.context[0])
    return length < self.maxNumTargets

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
    self.maxNumTargets = max(self.maxNumTargets, len(targets))
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
