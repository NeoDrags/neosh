from functions import execute_commands, ls, clear

def main():
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
    except KeyboardInterrupt:
        print("\nexit")
        

if __name__ == "__main__":
    main()
