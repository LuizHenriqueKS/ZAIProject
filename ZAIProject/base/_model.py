class Model:
  def fit(self, data, epochs: int, verbose: int = 1, tillAccuracy: float = None, tillLoss: float = None):
    raise NotImplementedError()

  def fitDataset(self, dataset, epochs: int, verbose: int = 1, tillAccuracy: float = None, tillLoss: float = None):
    raise NotImplementedError()

  def evaluate(self, data, context=None, table: bool = False, verbose: int = 1):
    raise NotImplementedError()

  def predict(self, data, context=None):
    raise NotImplementedError()
