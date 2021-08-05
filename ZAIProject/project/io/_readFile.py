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
  content = readContent(file)
  project.verbose = content['verbose']
  project.forceSingleValuePerOutput = content['forceSingleValuePerOutput']
  project.sharedData.data = content['sharedData']
  readIOSet(loaders, project, project.fit.input, content, ['fit', 'input'])
  readIOSet(loaders, project, project.fit.output, content, ['fit', 'output'])
  readIOSet(loaders, project, project.predict.input,
            content, ['predict', 'input'])
  readIOSet(loaders, project, project.predict.context,
            content, ['predict', 'context'])
  readIOSet(loaders, project, project.predict.output,
            content, ['predict', 'output'])
  if 'recursive' in content:
    project.recursive = loaders.load(
        'recursive', project, content['recursive'])
    project._dataApplier = RecursiveDataApplier(
        project, project._dataApplier, project.recursive)
  return project


def readIOSet(loaders, project, ioSet, content, keys):
  ioSetContent = getContentChild(content, keys)
  for ioName in ioSetContent.keys():
    io = ioSet.add()
    ioContent = ioSetContent[ioName]
    for processorName in ioContent.keys():
      processorContent = ioContent[processorName]
      io.add(readProcessor(loaders, project, processorContent))


def readProcessor(loaders, project, content):
  return loaders.load('processor', project, content)


def getContentChild(content, keys):
  result = content
  for key in keys:
    result = result[key]
  return result


def readContent(file):
  with open(file, 'r') as f:
    return json.load(f)
