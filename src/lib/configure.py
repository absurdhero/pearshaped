import os
import subprocess
import yaml


def find(directory):
    for name in [".ship.yml", ".travis.yml"]:
        if os.path.exists(os.path.join(directory, name)):
            return os.path.join(directory, name)


def parse(path):
    with open(path, 'r') as f:
        return yaml.load(f, Loader=yaml.BaseLoader)
