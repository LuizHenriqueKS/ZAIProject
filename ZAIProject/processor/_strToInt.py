from ..base._processor import Processor
from ..validation._requireStr import requireStr


class StrToInt(Processor):

    def __init__(self, reverse=None):
        super().__init__(reverse=reverse)

    def scale(self, data, project, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project, params=None):
        requireStr(data)
        return int(data)

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._intToStr import IntToStr
        return IntToStr()
