from ..base._model import Model


class TensorModel(Model):

    def __init__(self, project, model):
        self.project = project
        self.model = model
