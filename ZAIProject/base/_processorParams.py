from typing import Literal


class ProcessorParams:

  def __init__(self, mode: Literal['scale', 'fit', 'apply'], io: Literal['input', 'target', 'output'], contextIteration=0, context=None):
    self.mode = mode
    self.io = io
    self.contextIteration = contextIteration
    self.context = context
