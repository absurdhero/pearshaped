import subprocess
import os


def git(cmd):
    print("git " + cmd)
    return subprocess.check_call('/usr/bin/git ' + cmd, shell=True)


def sync(repo_base, url):
    if url is None or len(url) == 0:
        raise RuntimeError("repository url is empty")

    local_path = os.path.join(repo_base, 'repo')

    if os.path.exists(local_path):
        git("-C %s pull" % local_path)
    else:
        git("clone -- " + repr(url) + " " + local_path)

    print(local_path)
    return local_path
