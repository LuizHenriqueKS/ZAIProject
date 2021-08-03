from ..base._processor import Processor
from ..validation._requireStr import requireStr


class SplitStr(Processor):

    def __init__(self, separator: str, reverse):
        self.separator = separator
        self.reverseProcessor = reverse

    def scale(self, data, project, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project, params=None):
        requireStr(data)
        return data.split(self.separator)

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._joinStr import JoinStr
        return JoinStr(self.separator)

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        dataRecorder.record('separator', self.separator)
