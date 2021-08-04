from ..base._dataApplier import DataApplier
import tensorflow as tf


class TensorDataApplier(DataApplier):

    def __init__(self, project, parentApplier) -> None:
        super().__init__()
        self.project = project
        self.parentApplier = parentApplier

    def applyFitInput(self, data):
        raw = self.parentApplier.applyFitInput(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyFitTarget(self, data):
        raw = self.parentApplier.applyFitTarget(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def iterFitInput(self, data):
        return self.parentApplier.iterFitInput(data)

    def iterFitTarget(self, data):
        return self.parentApplier.iterFitTarget(data)

    def applyPredictInput(self, data):
        raw = self.parentApplier.applyPredictInput(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyPredictOutput(self, modelOutput, io: str):
        data = []
        if isinstance(modelOutput, list):
            data = [self.convertTensorToList(i) for i in modelOutput]
        if self.isTensorModelOutput(modelOutput):  # tensor model output
            data = modelOutput.tolist()
            if len(self.project.predict.output) == 1:
                data = [data]
        result = self.parentApplier.applyPredictOutput(data, io)
        if not isinstance(result, list):
            result = [result]
        return result

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
