from ..base._processor import Processor


class Output(Processor):

    def __init__(self, outputIndex: int, direction: str = 'right', size: int = None, sharedDataId=None, reverse=None):
        super().__init__(sharedDataId=sharedDataId, reverse=reverse)
        self.outputIndex = outputIndex
        self.size = size
        self.direction = direction

    def scale(self, data, project, params):
        return self.apply(data, project, params)

    def apply(self, data, project, params):
        output = params.lastOutputs[self.outputIndex]
        if self.size != None:
            if self.direction == 'right':
                output = output[-self.size:]
            elif self.direction == 'left':
                output = output[:self.size]
            else:
                raise NotImplementedError()
        return output
