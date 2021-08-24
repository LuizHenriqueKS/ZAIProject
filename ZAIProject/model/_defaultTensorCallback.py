import tensorflow as tf


class DefaultTensorCallback(tf.keras.callbacks.Callback):

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
      if 'accuracy' in key and 'val_' not in key:
        result.append(key)
    if len(result) == 0:
      return None
    return result
