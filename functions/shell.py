import subprocess
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
from git import Repo , InvalidGitRepositoryError

def shell():
            
    style = Style.from_dict({
        'username': '#0FFFFF bold',
        'dir': '#FFFFFF bold',
        'mid': '#0FFFFF bold',
        'parantheses1': '#FFFFFF bold',
        'git-branch': '#FF0000 bold',
        'star' : '#FFFF00 bold',
        'parantheses2': '#FFFFFF bold',
        'end': "#0FFFFF bold"
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
            
            x = subprocess.getoutput("git rev-parse --is-inside-work-tree")
            merged_completers = merge_completers([bash_commands, Files])

            part1 = ""
            part2 = ""
            part3 = ""
            part4 = ""
            part5 = ""
            part6 = ""
            part7 = ""
            part8 = ""
            
            if str(x) == "true":
                changed_files = subprocess.getoutput("git ls-files -m")
                added_files = subprocess.getoutput("git diff --name-only --cached")
                current_branch = subprocess.getoutput("git branch --show-current")
                if len(changed_files) != 0 or len(added_files) != 0:
                    part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
                    part2 = str(os.path.basename(str(os.getcwd())))
                    part3 = "]"
                    part4 = "("
                    part5 = current_branch + " "
                    part6 = "*"
                    part7 = ")"
                    part8 = "$ "
                else:
                    part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
                    part2 = str(os.path.basename(str(os.getcwd())))
                    part3 = "]"
                    part4 = "("
                    part5 = current_branch + " "
                    part6 = "✓"
                    part7 = ")"
                    part8 = "$ "                   
            else:
                part1 = "[" + str(getpass.getuser()) + "@" + hostname + " "
                part2 = str(os.path.basename(str(os.getcwd())))
                part3 = "]$ "
                    
                    
            input_required = [
                ('class:username', part1),
                ('class:dir', part2),
                ('class:mid', part3),
                ('class:parantheses1', part4),
                ('class:git-branch', part5),
                ('class:star', part6),
                ('class:parantheses', part7),
                ('class:end', part8)
            ]
            
            command = session.prompt(input_required,
                                     style=style,
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

        except InvalidGitRepositoryError:
            pass

        except EOFError:
            sys.exit("\nexit")
