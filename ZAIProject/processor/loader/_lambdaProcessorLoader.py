from ZAIProject.base import Loader
from .._lambda import Lambda


class LambdaProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Lambda.__name__

  def load(self, loaders, project, data):
    lambdaExpression = data['lambdaFunc']
    def lambdaFunc(x): return x
    return Lambda(
        lambdaFunc=lambdaFunc,
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
