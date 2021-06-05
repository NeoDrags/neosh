from pathlib import Path
from shutil import copytree, copyfile
from os.path import isdir

HOME_DIR = str(Path.home())
config_directory = HOME_DIR + "/.config"
yash_directory = HOME_DIR + "/.config/yash"
yaml_directory = yash_directory + "/config.yaml"

def checker():
    Path(config_directory).mkdir(parents=True, exist_ok=True)
    Path(yash_directory).mkdir(parents=True, exist_ok=True)
    if Path(yaml_directory).exists() != True:
        copyfile(".config/config.yaml", yaml_directory)
    themes_directory = yash_directory + "/themes"
    if isdir(themes_directory) != True:
        copytree("themes",themes_directory)
