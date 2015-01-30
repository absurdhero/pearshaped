import subprocess


class Docker():
    def __init__(self):
        self.committed = []

    def set_image(self, image):
        self.image = image

    def exec(self, command):
        print("docker " + command, flush=True)
        return subprocess.Popen("docker " + command,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                shell=True,
                                universal_newlines=True)

    def check_output(self, command):
        return subprocess.check_output('docker ' + command,
                                       shell=True,
                                       universal_newlines=True)

    def run_image(self, cmd='', flags=''):
        script = "docker run %s -i %s %s" % (flags, self.image, cmd)
        print(script, flush=True)
        return subprocess.Popen(
            script,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            universal_newlines=True)

    def commit_current_to(self, new_image):
        """ save the current/last running container to an image """
        ps = self.exec("ps -lq")
        ps.wait()
        self.container = ps.stdout.read().strip()

        commit = self.exec("commit %s %s" % (self.container, new_image))
        commit.wait()
        if commit.returncode != 0:
            raise RuntimeError(commit.stdout)

        self.committed.append(new_image)
        self.image = new_image

    def remove_all_committed(self):
        for image in self.committed:
            subprocess.check_call(['docker', 'rmi', '-f', image])
