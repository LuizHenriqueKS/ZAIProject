class Recursive:

  def splitTarget(self, mode, target):
    raise NotImplementedError()

  def convertOutputToContext(self, output):
    raise NotImplementedError()

  def getOutput(self, params):
    raise NotImplementedError()

  def canContinuePredict(self, params):
    raise NotImplementedError()

  def inspectParams(self, params):
    raise NotImplementedError()

  def saveData(self, dataRecorder):
    raise NotImplementedError()
