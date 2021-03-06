from ._custom import Custom
from typing import List
from ..processor._reverseSparse import ReverseSparse


class Sparse(Custom):

  def __init__(self, contextShape: List[int], maxLengthContext=0):
    super().__init__(ReverseSparse(), contextShape, maxLengthContext)
