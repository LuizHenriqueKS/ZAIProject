from ..base._processor import Processor
from ..validation._requireNumber import requireNumber


class IntToStr(Processor):

    def __init__(self, reverse=None):
        super().__init__(reverse=reverse)

    def scale(self, data, project=None, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project=None, params=None):
        requireNumber(data)
        return str(int(data))

    def reverse(self):
        if self.reverseProcessor == None:
            from ._strToInt import StrToInt
            return StrToInt()
        else:
            return self.reverseProcessor
