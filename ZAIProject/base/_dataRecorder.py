class DataRecorder:

  def __init__(self, data={}):
    self.data = data

  def recordBase(self, base) -> None:
    self.record('type', type(base).__name__)
    self.record('sharedDataId', base.sharedDataId)

  def record(self, name: str, value) -> None:
    self.data[name] = value

  def getChild(self, name: str):
    dataChild = {}
    self.record(name, dataChild)
    return DataRecorder(dataChild)
