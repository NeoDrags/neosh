from functions import execute_commands, ls, clear
from pathlib import Path
from pygments.lexers.shell import BashLexer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.completion import word_completer
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import os
from prompt_toolkit.styles import Style
import getpass
import socket

def main():
    style = Style.from_dict({

    # Prompt.
    'username': '#0FFFFF bold',
    'dir': '#FFFFFF bold',
    'end': '#0FFFFF bold'
    })

    HOME_DIR = str(Path.home())
    hostname = socket.gethostname()
    history = Path(HOME_DIR + "/.yash_history")
    session = PromptSession(history=FileHistory(str(history)))

    try:
        while True:
            part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
            part2 = str(os.path.basename(str(os.getcwd())))
            part3 = "]$ "
            input_required = [
                ('class:username', part1),
                ('class:dir', part2),
                ('class:end', part3)
            ]
            command = session.prompt(input_required, style=style, lexer=PygmentsLexer(BashLexer), auto_suggest=AutoSuggestFromHistory())
            
            
            if command == "exit":
                print("exit")
                break
            elif command == "ls":
                ls()
            elif len(command) == 0:
                pass
            elif command == "clear":
                clear()
            elif command == "help":
                print("yash : Yet Another SHell written in python.")
            else:
                execute_commands(command)
            command = command + "\n"
            
    except KeyboardInterrupt:
        print("\nexit")

if __name__ == "__main__":
    main()
