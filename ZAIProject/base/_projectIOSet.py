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

    def __len__(self):
        return len(self.ios)

    def __getitem__(self, index):
        return self.ios[index]

    def applyOne(self, data):
        result = []
        for io in self.ios:
            result.append(io.applyOne(data))
        return result

    def apply(self, data):
        result = []
        for one in data:
            result.append(self.applyOne(one))
        return result

    def applyPerIO(self, data):
        result = []
        for i in range(0, len(self.ios)):
            for j in range(0, len(data[i])):
                if len(result) <= i:
                    result.append([])
                ioResult = self.ios[i].applyOne(data[i][j])
                result[i].append(ioResult)
        return result
