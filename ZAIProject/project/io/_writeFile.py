from ZAIProject.base._dataRecorder import DataRecorder
import json
import numpy as np


def writeFile(project, file: str) -> None:
  dataRecorder = DataRecorder()
  project.saveData(dataRecorder)
  text = json.dumps(dataRecorder.data, cls=NumpyEncoder, indent=2)
  with open(file, 'w') as f:
    f.write(text)


class NumpyEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.integer):
      return int(obj)
    elif isinstance(obj, np.floating):
      return float(obj)
    elif isinstance(obj, np.ndarray):
      return obj.tolist()
    return json.JSONEncoder.default(self, obj)
