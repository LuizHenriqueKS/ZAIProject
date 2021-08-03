from ..base._processor import Processor
from ..validation._requireArray import requireArray


class JoinStr(Processor):

    def __init__(self, separator: str, reverse=None):
        super().__init__(reverse=reverse)
        self.separator = separator

    def scale(self, data, project, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project, params=None):
        requireArray(data)
        return self.separator.join(data)

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._splitStr import SplitStr
        return SplitStr(self.separator)

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        dataRecorder.record('separator', self.separator)
