from ..base._processor import Processor
from ..validation._requireStr import requireStr


class StrToInt(Processor):
    def scale(self, data, project, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project, params=None):
        requireStr(data)
        return int(data)

    def reverse(self):
        from ._intToStr import IntToStr
        return IntToStr()
