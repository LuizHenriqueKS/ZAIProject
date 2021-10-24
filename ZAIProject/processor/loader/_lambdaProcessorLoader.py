from ZAIProject.base import Loader
from .._lambda import Lambda


class LambdaProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == Lambda.__name__

  def load(self, loaders, project, data):
    lambdaExpression = self.tryGetData(data, 'lambdaFunc')
    def lambdaFunc(x): return x
    if lambdaExpression is not None:
      head = lambdaExpression[0][0]
      if '=' in head.split('=')[0]:
        index = head.index('=')
        lambdaFunc = self.parseFunc(lambdaExpression[index:].strip())
      else:
        lambdaFunc = self.parseFunc(''.join(lambdaExpression[0]))
    return Lambda(
        lambdaFunc=lambdaFunc,
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )

  def parseFunc(self, expression):
    env = {}
    exec(expression, env)
    methodName = list(env.keys())[-1]
    return env[methodName]
