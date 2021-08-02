from ._projectIOSet import ProjectIOSet


class ProjectFit:

    def __init__(self, project):
        self.input: ProjectIOSet = ProjectIOSet(project)
        self.output: ProjectIOSet = ProjectIOSet(project)
