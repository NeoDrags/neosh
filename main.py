from functions import execute_commands
from os import walk

def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("yash : Yet Another SHell written in python.")
        else:
            execute_commands(command)

if __name__ == "__main__":
    main()
