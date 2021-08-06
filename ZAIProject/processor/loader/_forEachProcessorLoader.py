from ZAIProject.base import Loader
from .._forEach import ForEach


class ForEachProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == ForEach.__name__

  def load(self, loaders, project, data):
    processores = []
    for key in data.keys():
      if key.startswith('processor'):
        processores.append(loaders.load('processor', project, data[key]))
    return ForEach(
        processores,
        data['sharedDataId'],
        loaders.tryLoadChild('processor', project, data, 'reverseProcessor'),
        self.tryGetData(data, 'name'),
    )
