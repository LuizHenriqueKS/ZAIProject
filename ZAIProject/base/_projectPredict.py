from ._projectIOSet import ProjectIOSet


class ProjectPredict:

    def __init__(self, project):
        self.project = project
        self.input: ProjectIOSet = ProjectIOSet(project)
        self.output: ProjectIOSet = ProjectIOSet(project)

    def baseFit(self):
        for i in self.project.fit.input:
            self.input.add().addAll(i)
        for i in self.project.fit.output:
            self.output.add().addAll(i.reverse())
        return self
