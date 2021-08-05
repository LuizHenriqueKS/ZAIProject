from ZAIProject.base._dataRecorder import DataRecorder
import json


def writeFile(project, file: str) -> None:
  dataRecorder = DataRecorder()
  project.saveData(dataRecorder)
  text = json.dumps(dataRecorder.data, indent=2)
  with open(file, 'w') as f:
    f.write(text)
