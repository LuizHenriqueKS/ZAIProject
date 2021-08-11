from ZAIProject.base import Loader
from .._ruleOf3d import RuleOf3D


class RuleOf3DProcessorLoader(Loader):

  def type(self):
    return 'processor'

  def canLoad(self, loaders, project, data) -> bool:
    return self.tryGetData(data, 'type') == RuleOf3D.__name__

  def load(self, loaders, project, data):
    return RuleOf3D(
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
