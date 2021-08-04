from tensorflow.python.framework.ops import convert_to_tensor
from ..base._model import Model
from ..base._project import Project
from typing import List
from ..utility._getShape import getShape
from ._tensorDataHelper import *
from ._defaultTensorCallback import DefaultTensorCallback
import tensorflow as tf


class TensorModel(Model):

  def __init__(self, project: Project, model: tf.keras.Model):
    self.project = project
    self.model = model

  def dataApplier(self):
    return self.project.dataApplier()

  def fit(self, data, epochs: int, verbose=None, callbacks: List[tf.keras.callbacks.Callback] = None, tillAccuracy: float = None, tillLoss: float = None):
    if isinstance(data, tf.data.Dataset):
      return self.fitDataset(data, epochs, verbose, callbacks, tillAccuracy, tillLoss)
    input = self.dataApplier().applyFitInput(data)
    target = self.dataApplier().applyFitTarget(data)
    modelInput = convertToTensors(input)
    modelTarget = convertToTensors(target)
    _callbacks = self.buildCallbacks(
        callbacks,
        tillAccuracy,
        tillLoss
    )
    return self.model.fit(modelInput,
                          modelTarget,
                          epochs=epochs,
                          verbose=self.getVerbose(verbose),
                          callbacks=_callbacks)

  def fitDataset(self, dataset, epochs: int, verbose=None, callbacks: List[tf.keras.callbacks.Callback] = None, tillAccuracy: float = None, tillLoss: float = None):
    _callbacks = self.buildCallbacks(
        callbacks,
        tillAccuracy,
        tillLoss
    )
    return self.model.fit(dataset,
                          epochs=epochs,
                          verbose=self.getVerbose(verbose),
                          callbacks=_callbacks)

  def predict(self, data, context=None):
    def myPredict(input):
      modelInput = convertToTensors(input)
      modelOutput = self.model.predict(modelInput)
      return convertFromTensors(self.project, modelOutput)
    result = self.dataApplier().runPredict(
        myPredict,
        data,
        context
    )
    for one in result:
      yield self.treatSingleOutput(one)

  def treatSingleOutput(self, one):
    if self.project.forceSingleValuePerOutput:
      while isinstance(one, list) and len(one) == 1:
        one = one[0]
    return one

  def evaluate(self, data, table: bool = False, verbose=1):
    input = self.dataApplier().applyFitInput(data)
    target = self.dataApplier().applyFitTarget(data)

    modelInput = convertToTensors(input)
    modelTarget = convertToTensors(target)

    if table:
      modelOutput = self.model.predict(modelInput)
      preOutput = convertFromTensors(self.project, modelOutput)
      target = self.dataApplier().applyPredictTarget(target)
      output = self.dataApplier().applyPredictOutput(preOutput)

      self.printAccuracy(data, target, output)

    return self.model.evaluate(modelInput, modelTarget, verbose=self.getVerbose(verbose))

  def getVerbose(self, verbose=None):
    if verbose == None:
      return self.project.verbose
    return verbose

  def printAccuracy(self, data, target, output):
    oks = 0
    for i in range(0, len(data)):
      log = f'{data[i]} '
      ok = True
      for j in range(0, len(target[i])):
        log += f'| {self.treatSingleOutput(target[i][j])} -> {self.treatSingleOutput(output[i][j])} '
        ok = ok and target[i][j] == output[i][j]
      if ok:
        log += '| OK'
        oks += 1
      else:
        log += '| Fail'
      print(log)
    print(f'Accuracy: {oks}/{len(data)}')

  def buildCallbacks(self, callbacks=None, tillAccuracy: float = None, tillLoss: float = None):
    result = []
    if callbacks != None:
      for callback in callbacks:
        result.append(callback)
    if tillAccuracy != None or tillLoss != None:
      result.append(
          DefaultTensorCallback(
              self.model,
              tillAccuracy,
              tillLoss
          )
      )
    return result
