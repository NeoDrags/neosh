from functions import execute_commands, ls, clear
from pathlib import Path
import readline
import os
from termcolor import colored
import getpass
import socket

def main():
    readline.parse_and_bind("tab: complete")
    HOME_DIR = str(Path.home())
    hostname = socket.gethostname()
    history = Path(HOME_DIR + "/.yash_history")
    if not history.is_file():
        readline.write_history_file(history)
    try:
        while True:
            cwd = str(os.path.basename(str(os.getcwd())))
            username = str(getpass.getuser())
            part1 = colored("[" + username + "@" + hostname, "cyan", attrs = ['bold'])
            part2 = colored(cwd, "white", attrs = ["bold"])
            part3 = colored("]$ ", "cyan", attrs = ["bold"])
            command = input(part1 + " " + part2 + part3)
            if command == "exit":
                print("exit")
                readline.append_history_file(1, history)
                break
            elif command == "ls":
                ls()
            elif command == "clear":
                clear()
            elif command == "help":
                print("yash : Yet Another SHell written in python.")
            else:
                execute_commands(command)
            command = command + "\n"
            readline.append_history_file(1, history)
            
    except KeyboardInterrupt:
        print("\nexit")

if __name__ == "__main__":
    main()
