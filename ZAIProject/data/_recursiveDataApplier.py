from ..base._dataApplier import DataApplier
from ..base._processorParams import ProcessorParams


class RecursiveDataApplier(DataApplier):

    def __init__(self, project, parentApplier, recursive):
        super().__init__()
        self.project = project
        self.parentApplier = parentApplier
        self.recursive = recursive

    def iterFitInput(self, data):
        for sample in data:
            iteration = 0
            params = ProcessorParams(
                mode='fit',
                io='input',
                iteration=iteration
            )
            fullTarget = self.applyFitTarget([sample])[0]
            targets = self.splitTarget(fullTarget)
            for target in targets:
                params.context.append(target)
                input = self.project.fit.input.applyOne(data, params)
                yield input, target

    def iterFitTarget(self, data):
        return self.parentApplier.iterFitTarget(data)

    def splitTarget(self, target):
        pass
