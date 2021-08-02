from ..base._processor import Processor
from ..validation._requireInt import requireInt


class IntToStr(Processor):
    def scale(self, data, project=None, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project=None, params=None):
        requireInt(data)
        return str(data)

    def reverse(self):
        from ._strToInt import StrToInt
        return StrToInt()
