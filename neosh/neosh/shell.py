import subprocess
from prompt_toolkit.shortcuts.prompt import prompt
from neosh.neosh.functions import execute_commands, ls, clear
from neosh.checker import checker, yaml_directory
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
import importlib
import yaml

def shell():
    HOME_DIR = str(Path.home())
    env = os.path.expanduser(os.path.expandvars(HOME_DIR + "/.config/neosh/Themes"))
    sys.path.append(env)
    checker()
    yaml_dir = open(yaml_directory, "r")
    yamlContents = yaml.load(yaml_dir, Loader = yaml.FullLoader)
    theme = importlib.import_module(yamlContents["theme"])
    history = Path(HOME_DIR + "/.neosh_history")
    session = PromptSession(history=FileHistory(str(history)))
    
    while True:
        try:
            importlib.reload(theme)
            bash_commands = WordCompleter([
                "ls",
                "cd",
                "clear",
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

            command = session.prompt(theme.input_required,
                                     style=theme.style,
                                     lexer=PygmentsLexer(FishShellLexer),
                                     auto_suggest=AutoSuggestFromHistory(),
                                     completer=FuzzyCompleter(merged_completers),
                                     complete_while_typing= False)
            

            if command == "exit":   
                print("exit")
                break
            elif command == "ls":
                ls()
            elif len(command) == 0:
                pass
            elif command == "clear":
                clear()
            elif command == "git commit":
                message = prompt("Enter Commit Message: ")
                subprocess.run("git commit -m \""+ message +"\"")
            elif command == "help":
                print("yash : Yet Another SHell written in python.")
            else:
                try:
                    try:
                        print(eval(command))
                    except:
                        out = exec(command)
                        if out != None:
                            print(out)
                except:
                    try:
                        execute_commands(command)
                    except:
                        os.system(command)
           
            command = command + "\n"


        except KeyboardInterrupt:
            sys.exit("\nexit")

        except EOFError:
            sys.exit("\nexit")
