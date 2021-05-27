import os
from os import system, name
import glob
from pathlib import Path
import subprocess
from termcolor import colored
from string import digits, ascii_letters as letters
from pathlib import Path
import os
import shutil

def execute_commands(command):
    try:
        commands = command.split()
        if "cd" == commands[0]:
            if len(commands[1:]) == 0:
                os.chdir(Path.home())
            else:
                cd(commands[1:])
            return
        elif "mkdir" == commands[0]:
            path = Path(os.getcwd())
            new_dir = os.path.join(path, commands[1])
            os.mkdir(new_dir)
            return
        elif "rm" == commands[0]:
            if commands[1] == "-rf":
                path = Path(os.getcwd())
                directory = os.path.join(path, commands[2])
                if os.path.exists(directory) and os.path.isdir(directory):
                    shutil.rmtree(directory, ignore_errors=True)
            else:
                os.remove(command[1])
            return


        subprocess.run(commands)
    except Exception:
        print("yash: command not found:", command)

def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def alphanumeric_key(text):
    return [c.lower() for c in text if c in letters + digits]

def ls():
    files = glob.glob("*")
    files.sort(key = alphanumeric_key)
    for file in files:
        if os.path.isdir(file):
            print(colored(file, 'blue', attrs=['bold']), end='   ')
        else:
            print(colored(file, "white", attrs=['bold']), end='   ')
    print()

def cd(path):
    ch = ''.join(path)
    try:
        os.chdir(os.path.abspath(ch))
    except Exception as e:
        print("cd: no such file or directory. ", e)
