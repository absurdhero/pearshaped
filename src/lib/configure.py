import os
import subprocess
import yaml


def find(directory):
    for name in [".pearshaped.yml", ".travis.yml"]:
        if os.path.exists(os.path.join(directory, name)):
            return os.path.join(directory, name)

    raise FileNotFoundError("could not find config file")


def parse(path):
    with open(path, 'r') as f:
        return yaml.load(f, Loader=yaml.BaseLoader)
