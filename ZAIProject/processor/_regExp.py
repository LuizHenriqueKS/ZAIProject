from ..base._processor import Processor
from ._noneProcessor import NoneProcessor
import re


class RegExp(Processor):
    def __init__(self, regexp: str):
        self.regexp = regexp

    def scale(self, data, project=None, params=None):
        return self.apply(data)

    def apply(self, data, project=None, params=None):
        regex = re.search(self.regexp, data)
        groups = regex.groups()
        return [i for i in groups]

    def reverse(self):
        return NoneProcessor(self)

    def saveData(self, dataRecorder) -> None:
        super().saveData(dataRecorder)
        dataRecorder.record('regexp', self.regexp)
