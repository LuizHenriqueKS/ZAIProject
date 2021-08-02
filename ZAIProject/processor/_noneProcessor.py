from ..base._processor import Processor


class NoneProcessor(Processor):

    def __init__(self, reverse: Processor = None):
        super().__init__()
        if (reverse == None):
            self._reverse = self
        else:
            self._reverse = reverse

    def scale(self, data, project=None, params = None):
        return self.apply(data)

    def apply(self, data, project=None, params=None):
        return data

    def reverse(self) -> Processor:
        return self.reverse

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        if (self.reverse != self):
            self.reverse.saveData(dataRecorder.getChild('reverse'))
