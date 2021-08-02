from ..base._processor import Processor
from ..validation._requireArray import requireArray


class ForEach(Processor):
    def __init__(self, processor: Processor):
        super().__init__()
        self.processor = processor

    def scale(self, data, project, params):
        requireArray(data)
        for i in data:
            self.processor.scale(i, project, params)

    def apply(self, data, project, params):
        requireArray(data)
        result = []
        for i in data:
            i2 = self.processor.apply(i, project, params)
            result.append(i2)
        return result

    def reverse(self):
        return ForEach(self.processor.reverse())

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        self.processor.saveData(dataRecorder.getChild('processor'))
