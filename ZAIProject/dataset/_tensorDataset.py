import tensorflow as tf
import random


def readSamples(project, samples, singleOutputs):
  def reader():
    inputIter = iter(project.dataApplier().iterApplyFitInput(samples))
    targetIter = iter(project.dataApplier().iterApplyFitTarget(samples))
    for input in inputIter:
      target = next(targetIter)
      if len(project.modelInfo.input) == 1:
        input = input[0]
      else:
        input = tuple(input)
      if len(project.modelInfo.output) == 1:
        target = target[0]
        if singleOutputs != None and (singleOutputs == True or singleOutputs[0]):
          target = target[0]
      else:
        if singleOutputs != None:
          for i in range(0, len(target)):
            if singleOutputs[i]:
              target[i] = target[i][0]
        target = tuple(target)
      yield input, target
  return reader


def TensorDataset(project, samples, singleOutputs=None, split: float = None):
  #print(next(iter(readSamples(project, samples, singleOutputs)())))
  if split != None:
    firstSamples, secondSamples = splitSamples(samples, split)
    first = tf.data.Dataset.from_generator(
        readSamples(project, firstSamples, singleOutputs),
        buildOutputShapes(project)
    )
    second = tf.data.Dataset.from_generator(
        readSamples(project, secondSamples, singleOutputs),
        buildOutputShapes(project)
    )
    return first, second
  else:
    dataset = tf.data.Dataset.from_generator(
        readSamples(project, samples, singleOutputs),
        buildOutputShapes(project)
    )
    return dataset


def splitSamples(samples, split: float):
  firstLength = round(len(samples) * split)
  secondLength = len(samples) - firstLength
  first = [i for i in samples]
  second = []
  while len(second) < secondLength:
    index = random.randrange(len(first))
    item = first[index]
    second.append(item)
    first.pop(index)
  return first, second


def buildOutputShapes(project):
  input = []
  output = []
  for i in range(0, len(project.modelInfo.input)):
    input.append(tf.float32)
  if len(project.modelInfo.input) == 1:
    input = input[0]
  else:
    input = tuple(input)
  for i in range(0, len(project.modelInfo.output)):
    output.append(tf.float32)
  if len(project.modelInfo.output) == 1:
    output = output[0]
  else:
    output = tuple(output)
  return (input, output)
