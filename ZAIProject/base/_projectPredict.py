from ._projectIOSet import ProjectIOSet


class ProjectPredict:

  def __init__(self, project):
    self.project = project
    self.input: ProjectIOSet = ProjectIOSet(project)
    self.context: ProjectIOSet = ProjectIOSet(project)
    self.output: ProjectIOSet = ProjectIOSet(project)

  def saveData(self, dataRecorder):
    self.input.saveData(dataRecorder.getChild('input'))
    self.context.saveData(dataRecorder.getChild('context'))
    self.output.saveData(dataRecorder.getChild('output'))

  def baseFit(self):
    for io in self.project.fit.input:
      self.input.add().addAll(io)
    for io in self.project.fit.output:
      self.context.add()
    for io in self.project.fit.output:
      self.output.add().addAll(io.reverse())
    return self
