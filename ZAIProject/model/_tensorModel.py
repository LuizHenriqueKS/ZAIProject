from tensorflow.python.framework.ops import convert_to_tensor
from ..base._model import Model
from ..base._project import Project
from typing import List
from ..utility._getShape import getShape
from ..data._tensorDataApplier import TensorDataApplier
import tensorflow as tf


class TensorModel(Model):

  def __init__(self, project: Project, model: tf.keras.Model):
    self.project = project
    self.model = model
    self.dataApplier = TensorDataApplier(project, project.dataApplier())

  def fit(self, data, epochs: int, verbose: int = 1, callbacks: List[tf.keras.callbacks.Callback] = None, tillAccuracy: float = None, tillLoss: float = None):
    if isinstance(data, tf.data.Dataset):
      return self.fitDataset(data, epochs, verbose, callbacks, tillAccuracy, tillLoss)
    modelInput = self.dataApplier.applyFitInput(data)
    modelTarget = self.dataApplier.applyFitTarget(data)
    _callbacks = self.buildCallbacks(
        callbacks, tillAccuracy, tillLoss)
    return self.model.fit(modelInput, modelTarget, epochs=epochs,
                          verbose=verbose,
                          callbacks=_callbacks)

  def fitDataset(self, dataset, epochs: int, verbose: int = 1, callbacks: List[tf.keras.callbacks.Callback] = None, tillAccuracy: float = None, tillLoss: float = None):
    _callbacks = self.buildCallbacks(
        callbacks, tillAccuracy, tillLoss)
    return self.model.fit(dataset, epochs=epochs,
                          verbose=verbose,
                          callbacks=_callbacks)

  def predict(self, data):
    modelInput = self.dataApplier.applyPredictInput(data)
    modelOutput = self.model.predict(modelInput)
    output = self.dataApplier.applyPredictOutput(modelOutput)
    return output

  def evaluate(self, data, verbose: bool = False):
    modelInput = self.dataApplier.applyFitInput(data)
    modelTarget = self.dataApplier.applyFitTarget(data)

    if verbose:
      modelOutput = self.model.predict(modelInput)
      target = self.dataApplier.applyPredictTarget(modelTarget)
      output = self.dataApplier.applyPredictOutput(modelOutput)
      self.printAccuracy(data, target, output)

    return self.model.evaluate(modelInput, modelTarget)

  def printAccuracy(self, data, target, output):
    oks = 0
    for i in range(0, len(data)):
      log = f'|{data[i]}'
      ok = True
      for j in range(0, len(target[i])):
        log += f'| {target[i][j]} -> {output[i][j]} '
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
      result.append(self.DefaultCallback(
          self.model, tillAccuracy, tillLoss))
    return result

  class DefaultCallback(tf.keras.callbacks.Callback):

    def __init__(self, model: tf.keras.Model, tillAccuracy=None, tillLoss=None):
      self.model = model
      self.tillAccuracy = tillAccuracy
      self.tillLoss = tillLoss
      self.accuracyReadable = True
      self.accuracyNames = None

    def on_epoch_end(self, epoch=None, logs=None):
      if self.tillAccuracy != None:
        accuracy = self.getAccuracy(logs)
        if accuracy != None:
          if accuracy >= self.tillAccuracy:
            self.model.stop_training = True
      if self.tillLoss != None:
        if logs['loss'] <= self.tillLoss:
          self.model.stop_training = True

    def getAccuracy(self, logs):
      if self.accuracyReadable:
        if self.accuracyNames == None:
          self.accuracyNames = self.getAccuracyNames(logs)
          if self.accuracyNames == None:
            self.accuracyReadable = False
        if self.accuracyReadable:
          result = 1
          for name in self.accuracyNames:
            result *= logs[name]
          return result

    def getAccuracyNames(self, logs):
      keys = logs.keys()
      result = []
      for key in keys:
        if 'accuracy' in key:
          result.append(key)
      if len(result) == 0:
        return None
      return result
