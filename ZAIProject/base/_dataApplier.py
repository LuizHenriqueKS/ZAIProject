class DataApplier:

  def iterScaleFitInputOne(self, one):
    raise NotImplementedError()

  def iterScaleFitTargetOne(self, one):
    raise NotImplementedError()

  def iterApplyFitInputOne(self, one):
    raise NotImplementedError()

  def iterApplyFitTargetOne(self, one):
    raise NotImplementedError()

  def iterApplyPredictInputOne(self, one):
    raise NotImplementedError()

  def iterApplyPredictTargetOne(self, one):
    raise NotImplementedError()

  def iterApplyPredictOutputOne(self, one):
    raise NotImplementedError()

  def runPredict(self, predictFunc, data, context):
    raise NotImplementedError()

  def iterApplyFitInput(self, data):
    for one in data:
      for input in self.iterApplyFitInputOne(one):
        yield input

  def iterApplyFitTarget(self, data):
    for one in data:
      for target in self.iterApplyFitTargetOne(one):
        yield target

  def iterApplyPredictInput(self, data):
    for one in data:
      for input in self.iterApplyPredictInputOne(one):
        yield input

  def iterApplyPredictTarget(self, data):
    for one in data:
      for target in self.iterApplyPredictTargetOne(one):
        yield target

  def iterApplyPredictOutput(self, data):
    for one in data:
      for output in self.iterApplyPredictOutputOne(one):
        yield output

  def scaleFitInputOne(self, one):
    return list(self.iterScaleFitInputOne(one))

  def scaleFitTargetOne(self, one):
    return list(self.iterScaleFitTargetOne(one))

  def applyFitInput(self, data):
    return list(self.iterApplyFitInput(data))

  def applyFitInputOne(self, one):
    return list(self.iterApplyFitInputOne(one))

  def applyFitTarget(self, data):
    return list(self.iterApplyFitTarget(data))

  def applyFitTargetOne(self, one):
    return list(self.iterApplyFitTargetOne(one))

  def applyPredictInput(self, data):
    return list(self.iterApplyPredictInput(data))

  def applyPredictInputOne(self, data):
    return list(self.iterApplyPredictInputOne(data))

  def applyPredictTarget(self, data):
    return list(self.iterApplyPredictTarget(data))

  def applyPredictTargetOne(self, data):
    return list(self.iterApplyPredictTargetOne(data))

  def applyPredictOutput(self, data):
    return list(self.iterApplyPredictOutput(data))

  def applyPredictOutputOne(self, data):
    return list(self.iterApplyPredictOutputOne(data))
