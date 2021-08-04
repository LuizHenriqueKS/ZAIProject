from ..base._processor import Processor


class Eraser1D(Processor):

    def __init__(self, direction, value=None, sharedDataId=None, reverse=None):
        super().__init__(sharedDataId=sharedDataId, reverse=reverse)
        self.direction = direction
        self.value = value

    def scale(self, data, project, params=None):
        raise NotImplementedError()

    def apply(self, data, project, params=None):
        try:
            result = []
            value = self.getValue(project)
            if self.direction == 'left':
                index = data.index(value)
                result = data[index:]
            elif self.direction == 'right':
                index = data.index(value)
                result = data[:index]
            else:
                raise NotImplementedError()
            return result
        except ValueError:
            return data

    def getValue(self, project):
        return self.getSharedData(project)['value']

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._autoPadding1D import AutoPadding1D
        return AutoPadding1D(direction=self.direction, value=self.value, sharedDataId=self.sharedDataId)

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        dataRecorder.record('direction', self.direction)
        dataRecorder.record('value', self.value)
