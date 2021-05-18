from functions import execute_commands, ls, clear
from pathlib import Path
import readline
import os

def main():
    readline.parse_and_bind("tab: complete")
    HOME_DIR = str(Path.home())
    history = Path(HOME_DIR + "/.yash_history")
    if not history.is_file():
        readline.write_history_file(history)
    try:
        while True:
            command = input("$ ")
            if command == "exit":
                print("exit")
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
