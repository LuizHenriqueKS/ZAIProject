class ProcessorParams:

    def __init__(self, mode: str, io: str, contextIteration=0, context=None):
        self.mode = mode
        self.io = io
        self.contextIteration = contextIteration
        self.context = context
