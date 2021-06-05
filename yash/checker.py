from pathlib import Path
<<<<<<< HEAD
from shutil import copyfile, move, copytree
from os.path import isdir, expanduser
from distutils.dir_util import copy_tree
=======
from shutil import copytree, copyfile
from os.path import isdir
>>>>>>> 802c6be6f17299987c8d0387d37f6880ebbc3c1e

home_dir = expanduser("~")
config_directory = home_dir + "/.config/"
yash_directory =config_directory+ "/yash"
yaml_directory = yash_directory + "/config.yaml"

def checker():
    Path(config_directory).mkdir(parents=True, exist_ok=True)
    Path(yash_directory).mkdir(parents=True, exist_ok=True)
    if Path(yaml_directory).exists() != True:
        copyfile(".config/config.yaml", yaml_directory)
<<<<<<< HEAD
    themes_directory = yash_directory + "/Themes"
    if isdir(themes_directory) != True:
        copy_tree("themes",themes_directory)
=======
    themes_directory = yash_directory + "/themes"
    if isdir(themes_directory) != True:
        copytree("themes",themes_directory)
>>>>>>> 802c6be6f17299987c8d0387d37f6880ebbc3c1e
