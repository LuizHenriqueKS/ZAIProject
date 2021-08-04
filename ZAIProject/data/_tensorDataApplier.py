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

    def applyPredictInput(self, data):
        raw = self.parentApplier.applyPredictInput(data)
        tensors = self.convertToTensors(raw)
        return tensors

    def applyPredictTarget(self, modelOutput):
        return self.applyPredictTargetOutput(modelOutput, io='target')

    def applyPredictOutput(self, modelOutput):
        return self.applyPredictTargetOutput(modelOutput, io='output')

    def applyPredictTargetOutput(self, modelOutput, io: str):
        data = []
        if isinstance(modelOutput, list):
            data = [self.convertTensorToList(i) for i in modelOutput]
        if self.isTensorModelOutput(modelOutput):
            data = modelOutput.tolist()
            if len(self.project.predict.output) == 1:
                data = [data]
        data = list(self.iterTransposePerIO(data))
        if io == 'output':
            result = self.parentApplier.applyPredictOutput(data)
        else:
            result = self.parentApplier.applyPredictTarget(data)
        if not isinstance(result, list):
            result = [result]
        return result

    def iterTransposePerIO(self, data):
        if len(data) != 0:
            dataLength = len(data[0])
            for i in range(0, dataLength):
                one = []
                for ioData in data:
                    one.append(ioData[i])
                yield one

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
