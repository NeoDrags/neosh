import os
from os import walk
import subprocess
from termcolor import colored

def execute_commands(command):
    try:
        commands = command.split()
        if "cd" == commands[0]:
            cd(commands[1:])
            return
        subprocess.run(commands)
    except Exception as e:
        print("Error command not found", e)

def ls():
    files = os.listdir()
    for file in files:
        if os.path.isfile(file) and file.startswith('.'):
            files.remove(file)
    files.sort(key=str.casefold)
    for file in files:
        if os.path.isdir(file):
            print(colored(file, 'blue', attrs=['bold']), end=' ')
        else:
            print(file, end=' ')
    print()

def cd(path):
    ch = ''.join(path)
    try:
        os.chdir(os.path.abspath(ch))
    except Exception as e:
        print("cd: no such file or directory. ", e)
