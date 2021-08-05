from ._loader import Loader
from ..error._loaderNotFoundError import LoaderNotFoundError


class Loaders:

  def __init__(self):
    self.loaders = []

  def addLoader(self, loader: Loader):
    self.loaders.append(loader)

  def load(self, type: str, project, data):
    for loader in self.loaders:
      if loader.type() == type:
        if loader.canLoad(self, project, data):
          return loader.load(self, project, data)
    raise LoaderNotFoundError(
        f"Loader not found for: type={type}, name={data['type']}"
    )

  def tryLoad(self, type: str, project, data):
    try:
      return self.load(type, project, data)
    except LoaderNotFoundError:
      return None

  def tryLoadChild(self, type: str, project, parentData, key):
    if key in parentData:
      return self.tryLoad(type, project, parentData[key])
    else:
      return None
