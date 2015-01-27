import os
import yaml

def each(home):
    with open(os.path.join(home, 'config.yml')) as projects_file:
        config = yaml.safe_load(projects_file)
        projects = config['projects']
        for name, properties in projects.items():
            yield Project(name, properties)

class Project():
    def __init__(self, name, properties):
        self.name = name
        self.repo_url = properties['repo']
