from ..base._processor import Processor
from ._noneProcessor import NoneProcessor
import re


class RegExp(Processor):
    def __init__(self, regexp: str, reverse=None):
        super().__init__(reverse=reverse)
        self.regexp = regexp

    def scale(self, data, project=None, params=None):
        return self.apply(data)

    def apply(self, data, project=None, params=None):
        regex = re.search(self.regexp, data)
        groups = regex.groups()
        return [i for i in groups]

    def reverse(self):
        if self.reverseProcessor == None:
            return NoneProcessor(self)
        else:
            return self.reverseProcessor

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        dataRecorder.record('regexp', self.regexp)
