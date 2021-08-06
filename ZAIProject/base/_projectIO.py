from ._processor import Processor
from typing import List
from ._processorParams import ProcessorParams


class ProjectIO:

  def __init__(self, project):
    self.processores = []
    self.project = project

  def saveData(self, dataRecorder):
    for i in range(0, len(self.processores)):
      self.processores[i].saveData(dataRecorder.getChild(f'processor{i}'))

  def add(self, processor: Processor):
    self.processores.append(processor)
    return self

  def clear(self):
    self.processores = []

  def removeByIndex(self, index: int):
    self.processores.pop(index)

  def removeLast(self):
    self.processores.pop()

  def insert(self, index: int, processor: Processor):
    self.processores.insert(index, processor)
    return self

  def addAll(self, processores):
    for p in processores:
      self.add(p)
    return self

  def reverse(self) -> List[Processor]:
    result = []
    for i in self.processores:
      result.insert(0, i.reverse())
    return result

  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    if self.index >= len(self.processores):
      raise StopIteration
    else:
      item = self.processores[self.index]
      self.index += 1
      return item

  def applyOne(self, data, params=None):
    result = data
    for processor in self.processores:
      result = processor.apply(result, self.project, params)
    return result

  def scaleOne(self, data, params=None):
    result = data
    for processor in self.processores:
      result = processor.scale(result, self.project, params)
    return result
