from typing import Literal


class Loader:

  def type() -> Literal['processor', 'recursive']:
    raise NotImplementedError()

  def canLoad(self, loaders, project, data) -> bool:
    raise NotImplementedError()

  def load(self, loaders, project, data):
    raise NotImplementedError()
