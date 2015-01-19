import os
import subprocess
import yaml


def find_config(directory):
    for name in [".ship.yml", ".travis.yml"]:
        if os.path.exists(os.path.join(directory, name)):
            return os.path.join(directory, name)


def parse_shipconfig(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def run(config):
    success = True

    step_order = ['before_install', 'install', 'before_script', 'script']
    for name in step_order:
        success = execute_step(config, name)
        if not success:
            break

    if success:
        execute_step(config, 'after_success')
    else:
        execute_step(config, 'after_failure')

    execute_step(config, 'after_script')

    return success


def execute_step(config, name):
    if name in config:
        print("executing step %s" % name)

        env = os.environ.copy()
        env.update(EXTRA_ENV)

        if isinstance(config[name], str):
            commands = [config[name]]
        else:
            commands = config[name]

        returncode = subprocess.call(
            ['/bin/bash', '-x', '-e', '-c', '; '.join(commands)],
            env=env)
        if returncode != 0:
            print("failed during '%s' step" % name)
            return False

    return True


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
