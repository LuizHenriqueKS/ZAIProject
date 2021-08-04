class Model:
    def fit(self, data, epochs: int, verbose: int = 1, tillAccuracy: float = None, tillLoss: float = None):
        pass

    def fitDataset(self, dataset, epochs: int, verbose: int = 1, tillAccuracy: float = None, tillLoss: float = None):
        pass

    def evaluate(self, data):
        pass
