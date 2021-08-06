import ZAIProject
from ZAIProject import loader
from ZAIProject.project import Project
from ZAIProject.base import Loaders
from ZAIProject.loader import DefaultLoaders
from ZAIProject.data import RecursiveDataApplier
import json


def readFile(file: str, loaders: Loaders = None) -> Project:
  if loaders == None:
    loaders = DefaultLoaders()
  project = Project()
  data = readData(file)
  project.verbose = data['verbose']
  project.forceSingleOutput = data['forceSingleOutput']
  project.sharedData.data = data['sharedData']
  readIOSet(loaders, project, project.fit.input, data, ['fit', 'input'])
  readIOSet(loaders, project, project.fit.output, data, ['fit', 'output'])
  readIOSet(loaders, project, project.predict.input,
            data, ['predict', 'input'])
  readIOSet(loaders, project, project.predict.context,
            data, ['predict', 'context'])
  readIOSet(loaders, project, project.predict.output,
            data, ['predict', 'output'])
  if 'recursive' in data:
    project.recursive = loaders.load(
        'recursive', project, data['recursive'])
    project._dataApplier = RecursiveDataApplier(
        project, project._dataApplier, project.recursive)
  project.modelInfo = loaders.load('modelInfo', project, data['modelInfo'])
  return project


def readIOSet(loaders, project, ioSet, data, keys):
  ioSetContent = getDataChild(data, keys)
  for ioName in ioSetContent.keys():
    io = ioSet.add()
    ioContent = ioSetContent[ioName]
    for processorName in ioContent.keys():
      processorContent = ioContent[processorName]
      io.add(readProcessor(loaders, project, processorContent))


def readProcessor(loaders, project, data):
  return loaders.load('processor', project, data)


def getDataChild(data, keys):
  result = data
  for key in keys:
    result = result[key]
  return result


def readData(file):
  with open(file, 'r') as f:
    return json.load(f)
