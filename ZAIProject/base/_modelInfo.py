from ._ioInfo import IOInfo
from typing import List


class ModelInfo:
    def __init__(self):
        self.input: List[IOInfo] = []
        self.output: List[IOInfo]= []
        pass
