import os
import subprocess

def execute_commands(command):
    try:
        commands = command.split()
        if "cd" == commands[0]:
            cd(commands[1:])
            return
        subprocess.run(commands)
    except Exception as e:
        print("Error command not found", e)

def cd(path):
    ch = ''.join(path)
    try:
        os.chdir(os.path.abspath(ch))
    except Exception as e:
        print("cd: no such file or directory. ", e)
