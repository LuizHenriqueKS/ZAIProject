from ..base._dataApplier import DataApplier
from ..base._processorParams import ProcessorParams


class DefaultDataApplier(DataApplier):

    def __init__(self, project) -> None:
        super().__init__()
        self.project = project

    def applyFitInput(self, data):
        params = ProcessorParams(mode='fit', io='input')
        result = self.project.fit.input.apply(data, params)
        return result

    def applyFitTarget(self, data):
        params = ProcessorParams(mode='fit', io='target')
        result = self.project.fit.output.apply(data, params)
        return result

    def iterFitInput(self, data):
        params = ProcessorParams(mode='fit', io='input')
        for one in data:
            yield self.project.fit.input.applyOne(one, params)

    def iterFitTarget(self, data):
        params = ProcessorParams(mode='fit', io='target')
        for one in data:
            yield self.project.fit.output.applyOne(one, params)

    def applyPredictInput(self, data):
        params = ProcessorParams(mode='predict', io='input')
        result = self.project.predict.input.apply(data, params)
        return result

    def applyPredictOutput(self, data, io: str):
        params = ProcessorParams(mode='predict', io=io)
        return self.project.predict.output.applyPerIO(data, params)
