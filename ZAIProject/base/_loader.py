from typing import Literal


class Loader:

  def type() -> Literal['processor', 'recursive', 'modelInfo']:
    raise NotImplementedError()

  def canLoad(self, loaders, project, data) -> bool:
    raise NotImplementedError()

  def load(self, loaders, project, data):
    raise NotImplementedError()

  def tryGetData(self, data, key: str):
    if key in data:
      return data[key]
    return None
