from ._projectIO import ProjectIO
from typing import List


class ProjectIOSet:

    def __init__(self, project):
        self.ios: List[ProjectIO] = []
        self.project = project

    def add(self, io: ProjectIO = None) -> ProjectIO:
        if io == None:
            io = ProjectIO(self.project)
        self.ios.append(io)
        return io

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.ios):
            raise StopIteration
        else:
            item = self.ios[self.index]
            self.index += 1
            return item

    def applyOne(self, data):
        result = []
        for i in self.ios:
            result.append(i.applyOne(data))
        return result

    def apply(self, data):
        result = []
        for i in data:
            result.append(self.applyOne(i))
        return result
