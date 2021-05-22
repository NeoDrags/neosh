from functions.functions import execute_commands, ls, clear
from pathlib import Path
from pygments.lexers.shell import FishShellLexer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import sys
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import os
from prompt_toolkit.styles import Style
import getpass
import socket


def shell():
    style = Style.from_dict({
    'username': '#0FFFFF bold',
    'dir': '#FFFFFF bold',
    'end': '#0FFFFF bold'
    })
    
    HOME_DIR = str(Path.home())
    hostname = socket.gethostname()
    history = Path(HOME_DIR + "/.yash_history")
    session = PromptSession(history=FileHistory(str(history)))

    while True:
        try:
            
            part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
            part2 = str(os.path.basename(str(os.getcwd())))
            part3 = "]$ "
            input_required = [
                ('class:username', part1),
                ('class:dir', part2),
                ('class:end', part3)
            ]
            
            command = session.prompt(input_required, style=style, lexer=PygmentsLexer(FishShellLexer), auto_suggest=AutoSuggestFromHistory())
            
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
            sys.exit("\nexit")

        except EOFError:
            sys.exit("\nexit")
