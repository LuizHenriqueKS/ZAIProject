from random import random

from tensorflow.python.framework.ops import convert_to_tensor
from ..base._model import Model
from ..base._project import Project
import tensorflow as tf
from typing import List
from ..utility._getShape import getShape


class TensorModel(Model):

    def __init__(self, project: Project, model: tf.keras.Model):
        self.project = project
        self.model = model

    def fit(self, data, epochs: int, verbose: int = 1, callbacks: List[tf.keras.callbacks.Callback] = None, tillAccuracy: float = None, tillLoss: float = None):
        modelInput = self.applyFitInput(data)
        modelTarget = self.applyFitOutput(data)
        _callbacks = self.buildCallbacks(
            callbacks, tillAccuracy, tillLoss)
        return self.model.fit(modelInput, modelTarget, epochs=epochs,
                              verbose=verbose,
                              callbacks=_callbacks)

    def predict(self, data):
        modelInput = self.applyPredictInput(data)
        modelOutput = self.model.predict(modelInput)
        output = self.applyPredictOutput(modelOutput)
        return output

    def evaluate(self, data, verbose: bool = False):
        modelInput = self.applyFitInput(data)
        modelTarget = self.applyFitOutput(data)

        if verbose:
            modelOutput = self.model.predict(modelInput)
            target = self.applyPredictOutput(modelTarget)
            output = self.applyPredictOutput(modelOutput)
            oks = 0
            for i in range(0, len(data)):
                log = f'|{data[i]}'
                ok = True
                for j in range(0, len(target)):
                    log += f'| {target[j][i]} -> {output[j][i]} '
                    ok = ok and target[j][i] == output[j][i]
                if ok:
                    log += '| OK'
                    oks += 1
                else:
                    log += '| Fail'
                print(log)
            print(f'Accuracy: {oks}/{len(data)}')

        return self.model.evaluate(modelInput, modelTarget)

    def applyFitInput(self, data):
        raw = self.project.fit.input.apply(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyFitOutput(self, data):
        raw = self.project.fit.output.apply(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyPredictInput(self, data):
        raw = self.project.predict.input.apply(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyPredictOutput(self, modelOutput):
        data = []
        if isinstance(modelOutput, list):
            data = [self.convertTensorToList(i) for i in modelOutput]
        if self.isTensorModelOutput(modelOutput):  # tensor model output
            data = modelOutput.tolist()
            if len(self.project.predict.output) == 1:
                data = [data]
        return self.project.predict.output.applyPerIO(data)

    def isTensorModelOutput(self, data):
        return type(data).__name__ == 'ndarray'

    def convertTensorToList(self, tensor):
        if hasattr(tensor, 'numpy'):
            return tensor.numpy().tolist()
        elif hasattr(tensor, 'tolist'):
            return tensor.tolist()
        return tensor

    def convertToTensors(self, data):
        result = []
        for one in data:
            for i in range(0, len(one)):
                if len(result) <= i:
                    result.append([])
                result[i].append(one[i])
        return [tf.convert_to_tensor(i) for i in result]

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

        def on_epoch_end(self, logs=None):
            if self.tillAccuracy != None:
                if hasattr(logs, 'acc'):
                    if logs.acc >= self.tillAccuracy:
                        self.model.stop_training = True
            if self.tillLoss != None:
                if self.loss <= self.tillLoss:
                    self.model.stop_training = True
