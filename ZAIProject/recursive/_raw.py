from ._custom import Custom
from ..processor._noneProcessor import NoneProcessor
from typing import List


class Raw(Custom):
  def __init__(self, contextShape: List[int]):
    super().__init__(NoneProcessor(), contextShape)
