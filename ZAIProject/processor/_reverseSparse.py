from ..base._processor import Processor
from ..validation._isFloat import isFloat
from ..validation._requireNumberArray import requireNumberArray
from ..utility._getBestIndex import getBestIndex


class ReverseSparse(Processor):

  def scale(self, data, project, params):
    return self.apply(data, project, params)

  def apply(self, data, project=None, params=None):
    if params == None or params.io != 'target':
      if isFloat(data[0]):
        return [getBestIndex(data)]
      else:
        requireNumberArray(data[0])
        return [getBestIndex(i) for i in data]
    return data

  def reverse(self):
    if self.reverseProcessor != None:
      return self.reverseProcessor
    from ._sparse import Sparse
    return Sparse()
