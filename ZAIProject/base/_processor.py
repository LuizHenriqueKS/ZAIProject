from ._processorParams import ProcessorParams
from ._dataRecorder import DataRecorder
import random


class Processor:

    def __init__(self):
        self.sharedDataId = random.random()

    def scale(self, data, project, params: ProcessorParams = None):
        pass

    def apply(self, data, project, params: ProcessorParams = None):
        pass

    def reverse(self):
        pass

    def saveData(self, dataRecorder: DataRecorder) -> None:
        dataRecorder.recordBase(self)
        pass
