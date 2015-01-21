import os
import subprocess
import shutil


class Executor():
    # uniquely identifies each built image during this session
    global_id = 1

    def __init__(self, host_repo_path, repo_dir, config):
        self.host_repo_path = host_repo_path
        self.repo_dir = repo_dir
        self.config = config
        self.build_id = self.global_id
        self.global_id += 1

    def label(self):
        return "build" + str(self.build_id)

    def run(self):
        success = True

        self.image = self._toolchain_container()
        self.container = self.image

        step_order = ['before_install', 'install', 'before_script', 'script']
        for name in step_order:
            success = self.execute_step(name)
            if not success:
                break

        if success:
            self.execute_step('after_success')
        else:
            self.execute_step('after_failure')

        self.execute_step('after_script')

        return success

    def execute_step(self, name):

        if name in self.config:
            print("executing step %s" % name)

            env = os.environ.copy()
            env.update(self.EXTRA_ENV)

            if isinstance(self.config[name], str):
                commands = [self.config[name]]
            else:
                commands = self.config[name]

            script = ["set -e -x", 'cd "%s"' % self.repo_dir] + commands

            sh = self._run_image(self.image)
            sh.stdin.write(";\n".join(script))

            sh.stdin.close()
            sh.wait()

            if sh.returncode != 0:
                print("failed during '%s' step" % name)
                return False
            else:
                try:
                    self._commit_container(name)
                except Error:
                    print("failed to commit %s on step %s" % (self.container, name))
                    return False

        return True

    def _docker(self, command):
        print("docker " + command)
        return subprocess.Popen("docker " + command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                shell=True,
                universal_newlines=True)

    def _run_image(self, image, cmd=''):
        script = "docker run -v \"%s\":/repos -i %s %s" % (self.host_repo_path, image, cmd)
        print(script)
        return subprocess.Popen(
                script,
                stdin=subprocess.PIPE,
                shell=True,
                universal_newlines=True)

    def _commit_container(self, name):
        ps = self._docker("ps -lq")
        ps.wait()
        self.container = ps.stdout.read().strip()

        new_image =  "%s-%s" % (self.label(), name)
        self.image = new_image
        commit = self._docker("commit %s %s" % (self.container, new_image))
        commit.wait()
        if commit.returncode != 0:
            raise Error(commit.stdout)

    def _toolchain_container(self):
        if 'language' in self.config:
            return 'shipbuilder-language-' + self.config['language']

        return "shipbuilder-base"


    EXTRA_ENV = {
        'CI': 'true',
        'TRAVIS': 'true',
        'CONTINUOUS_INTEGRATION': 'true',
        'DEBIAN_FRONTEND': 'noninteractive',
        'LANG': 'en_US.UTF-8',
        'LC_ALL': 'en_US.UTF-8',
        'RAILS_ENV': 'test',
        'RACK_ENV': 'test',
        'MERB_ENV': 'test',
        'JRUBY_OPTS': '--server -Dcext.enabled=false -Xcompile.invokedynamic=false'
    }
