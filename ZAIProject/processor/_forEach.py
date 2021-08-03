from tensorflow.python.ops.gen_array_ops import reverse
from ZAIProject import processor
from ..base._processor import Processor
from ..validation._requireArray import requireArray


class ForEach(Processor):
    def __init__(self, processores, reverse=None):
        super().__init__(reverse=reverse)
        if isinstance(processores, Processor):
            self.processores = [processores]
        else:
            self.processores = processores

    def scale(self, data, project, params):
        requireArray(data)
        for one in data:
            processorResult = one
            for processor in self.processores:
                processorResult = processor.scale(
                    processorResult, project, params)

    def apply(self, data, project, params):
        requireArray(data)
        result = []
        for one in data:
            processorResult = one
            for processor in self.processores:
                processorResult = processor.apply(
                    processorResult, project, params)
            result.append(processorResult)
        return result

    def reverse(self):
        reversedProcessores = [p.reverse() for p in self.processores]
        reversedProcessores.reverse()
        return ForEach(reversedProcessores)

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        for i in range(0, len(self.processores)):
            processor = self.processores[i]
            dataRecorderChild = dataRecorder.getChild(f'processor{i}')
            processor.saveData(dataRecorderChild)
