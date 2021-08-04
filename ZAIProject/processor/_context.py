from ..base._processor import Processor


class Context(Processor):

    def __init__(self, contextIndex: int, returnSequences=False, sharedDataId=None, reverse=None):
        super().__init__(sharedDataId=sharedDataId, reverse=reverse)
        self.contextIndex = contextIndex
        self.returnSequences = returnSequences

    def scale(self, data, project, params):
        return self.apply(data, project, params)

    def apply(self, data, project, params):
        if len(params.context) == 0:
            return []
        context = params.context[self.contextIndex]
        if not self.returnSequences:
            if len(context) == 0:
                return []
            return context[len(context) - 1]
        return context
