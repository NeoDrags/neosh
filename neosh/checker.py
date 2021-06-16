from pathlib import Path
from shutil import copyfile
from os.path import isdir, expanduser, dirname, realpath
from distutils.dir_util import copy_tree
from os import name

home_dir = expanduser("~")
config_directory = home_dir + "/.config/"
yash_directory =config_directory+ "/neosh"
yaml_directory = yash_directory + "/config.yaml"
file_location = dirname(realpath(__file__))


def checker():
    Path(config_directory).mkdir(parents=True, exist_ok=True)
    Path(yash_directory).mkdir(parents=True, exist_ok=True)
    if Path(yaml_directory).exists() != True:
        copyfile(file_location + "/neosh/config.yaml", yaml_directory)
    themes_directory = yash_directory + "/Themes"
    if isdir(themes_directory) != True:
        copy_tree(file_location + "/themes",themes_directory)
