from ..base._recursive import Recursive


class Sparse(Recursive):

    def __init__(self, contextShape):
        super().__init__()
        self.contextShape = contextShape
