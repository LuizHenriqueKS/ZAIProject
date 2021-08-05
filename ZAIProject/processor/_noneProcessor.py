from ..base._processor import Processor


class NoneProcessor(Processor):

  def __init__(self, sharedDataId=None, reverse: Processor = None):
    super().__init__(sharedDataId=sharedDataId, reverse=reverse)

  def scale(self, data, project=None, params=None):
    return self.apply(data)

  def apply(self, data, project=None, params=None):
    return data

  def reverse(self) -> Processor:
    if self.reverseProcessor == None:
      return self
    return self.reverseProcessor
