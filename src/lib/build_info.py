import os
import sh


class BuildInfo():
    def __init__(self, host_repo_path, project_dir, build_id, config):
        self.host_repo_path = host_repo_path
        self.project_dir = project_dir
        self.build_id = build_id
        self.config = config

        self.repo_dir = os.path.join(self.project_dir, 'repo')
        self.build_dir = os.path.join(project_dir, 'builds', build_id)

    def commit_id(self):
        return str(sh.git('-C', self.repo_dir, 'rev-parse', 'HEAD')).strip()
