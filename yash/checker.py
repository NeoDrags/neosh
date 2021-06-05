from pathlib import Path
from shutil import copyfile, move, copytree
from os.path import isdir, expanduser
from distutils.dir_util import copy_tree

home_dir = expanduser("~")
config_directory = home_dir + "/.config/"
yash_directory =config_directory+ "/yash"
yaml_directory = yash_directory + "/config.yaml"

def checker():
    Path(config_directory).mkdir(parents=True, exist_ok=True)
    Path(yash_directory).mkdir(parents=True, exist_ok=True)
    if Path(yaml_directory).exists() != True:
        copyfile(".config/config.yaml", yaml_directory)
    themes_directory = yash_directory + "/Themes"
    if isdir(themes_directory) != True:
        copy_tree("themes",themes_directory)
