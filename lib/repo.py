import subprocess
import os


repo_dir = "/repos/repo"


def git(cmd):
    print("git " + cmd)
    return subprocess.call('/usr/bin/git ' + cmd, shell=True)


def sync():
    if os.path.exists(repo_dir):
        git("-C %s pull" % repo_dir)
    else:
        git("clone -- " + repr(os.getenv("REPO_URL")) + " " + repo_dir)

    return repo_dir
