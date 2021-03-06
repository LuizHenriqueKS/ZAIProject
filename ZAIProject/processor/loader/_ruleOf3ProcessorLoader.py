from ZAIProject.base import Loader
from .._ruleOf3 import RuleOf3


class RuleOf3ProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == RuleOf3.__name__

  def load(self, loaders, project, data):
    return RuleOf3(
        minInput=data['minInput'],
        maxInput=data['maxInput'],
        minOutput=data['minOutput'],
        maxOutput=data['maxOutput'],
        sharedDataId=data['sharedDataId'],
        reverse=loaders.tryLoadChild(
            'processor', project, data, 'reverseProcessor'
        ),
        name=self.tryGetData(data, 'name'),
    )
