class Model:
  def fit(self, data, epochs: int, verbose=None, tillAccuracy: float = None, tillLoss: float = None):
    raise NotImplementedError()

  def fitDataset(self, dataset, epochs: int, verbose=None, tillAccuracy: float = None, tillLoss: float = None):
    raise NotImplementedError()

  def evaluate(self, data, context=None, table: bool = False, verbose=None):
    raise NotImplementedError()

  def predict(self, data, context=None):
    raise NotImplementedError()

  def predictOne(self, data, context=None):
    return self.predict([data], [context])[0]
