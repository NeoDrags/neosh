from prompt_toolkit.shortcuts.prompt import CompleteStyle
from functions.functions import execute_commands, ls, clear
from pathlib import Path
from pygments.lexers.shell import FishShellLexer
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import FuzzyCompleter
import sys
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import os
from prompt_toolkit.completion import merge_completers, WordCompleter
import glob
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
            bash_commands = WordCompleter([
                "ls",
                "cd",
                "cat",
                "python3",
                "python",
                "pip3",
                "pip",
                "exit",
                "neofetch",
                "sudo",
                "su"
            ])
            Files = WordCompleter(glob.glob("*"))
            
            merged_completers = merge_completers([bash_commands, Files])
            part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
            part2 = str(os.path.basename(str(os.getcwd())))
            part3 = "]$ "
            input_required = [
                ('class:username', part1),
                ('class:dir', part2),
                ('class:end', part3)
            ]
            
            command = session.prompt(input_required,
                                     style=style,
                                     lexer=PygmentsLexer(FishShellLexer),
                                     auto_suggest=AutoSuggestFromHistory(),
                                     completer=FuzzyCompleter(merged_completers),
                                     complete_style=CompleteStyle.READLINE_LIKE)

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
