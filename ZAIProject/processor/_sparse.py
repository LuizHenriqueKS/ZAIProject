from ..base._processor import Processor


class Sparse(Processor):

    def scale(self, data, project=None, params=None):
        return self.apply(data, project, params)

    def apply(self, data, project=None, params=None):
        return data

    def reverse(self):
        if self.reverseProcessor != None:
            return self.reverseProcessor
        from ._reverseSparse import ReverseSparse
        return ReverseSparse()
