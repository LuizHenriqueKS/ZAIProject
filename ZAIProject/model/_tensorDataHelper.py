import tensorflow as tf


def convertFromTensors(project, modelOutput):
  data = []
  if isinstance(modelOutput, list):
    data = [convertTensorToList(i) for i in modelOutput]
  if isTensorModelOutput(modelOutput):
    data = modelOutput.tolist()
    if len(project.predict.output) == 1:
      data = [data]
  data = list(iterTransposePerIO(data))
  return data


def iterTransposePerIO(data):
  if len(data) != 0:
    dataLength = len(data[0])
    for i in range(0, dataLength):
      one = []
      for ioData in data:
        one.append(ioData[i])
      yield one


def isTensorModelOutput(data):
  return type(data).__name__ == 'ndarray'


def convertTensorToList(tensor):
  if hasattr(tensor, 'numpy'):
    return tensor.numpy().tolist()
  elif hasattr(tensor, 'tolist'):
    return tensor.tolist()
  return tensor


def convertToTensors(data):
  result = []
  for one in data:
    for i in range(0, len(one)):
      if len(result) <= i:
        result.append([])
      result[i].append(one[i])
  return [tf.convert_to_tensor(i) for i in result]
