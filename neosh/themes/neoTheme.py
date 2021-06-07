import os
import subprocess
from prompt_toolkit.styles import Style
from pathlib import Path
from socket import gethostname
import getpass
import shutil
from datetime import datetime

style = Style.from_dict({
    'parantheses1': '#FFFFFF bold',
    'username': '#FF0000 bold',
    'parantheses2': '#FFFFFF bold',
    'parantheses3': '#FFFFFF bold',
    'hostname': '#00FF00 bold',
    'pipe': '#FFFFFF bold',
    'date-time': '#0FFFFF bold',
    'parantheses4': '#FFFFFF bold',
    'parantheses5': '#FFFFFF bold',
    'git-branch': '#0000FF bold',
    'star' : '#FFFF00 bold',
    'parantheses6': '#FFFFFF bold',
    'end': "#FFFF00 bold"
})

HOME_DIR = str(Path.home())
hostname = str(gethostname())
history = Path(HOME_DIR + "/.yash_history")

x = subprocess.getoutput("git rev-parse --is-inside-work-tree")

rightNow = datetime.now()
now = rightNow.strftime("%d/%m/%Y %H:%M:%S")

part1=""
part2=""
part3=""
part4=""
part5=""
part6=""
part7=""
part8=""
part9=""
part10=""
part11=""
part12=""
part13=""

if str(x) == "true":
    changed_files = subprocess.getoutput("git ls-files -m")
    added_files = subprocess.getoutput("git diff --name-only --cached")
    current_branch = subprocess.getoutput("git branch --show-current")
    noOfColumns = shutil.get_terminal_size()[0]
    if len(changed_files) != 0 or len(added_files) != 0:
        part1 = "(" 
        part2 = str(getpass.getuser()) + "@" + str(os.path.basename(os.getcwd()))
        part3 = ")"
        part5 = hostname
        part6 =" | "
        part7 = now
        part8 = ")" + "\n"
        new_str = part1 + part2 + part3 + part5 + part6 + part7 + part8
        width = noOfColumns - len(new_str) -1
        part4 = "(".rjust(width, "-")
        part9 = "("
        part10 = current_branch + " "
        part11 = "*"
        part12 = ")"
        part13 = "$ "
    else:        
        part1 = "(" 
        part2 = str(getpass.getuser()) + "@" + str(os.path.basename(os.getcwd()))
        part3 = ")"
        part5 = hostname
        part6 =" | "
        part7 = now
        part8 = ")" + "\n"
        new_str = part1 + part2 + part3 + part5 + part6 + part7 + part8
        width = noOfColumns - len(new_str) -1
        part4 = "(".rjust(width, "-")
        part9 = "("
        part10 = current_branch + " "
        part11 = "✔"
        part12 = ")"
        part13 = "$ "                 
else:    
    noOfColumns = shutil.get_terminal_size()[0]
    part1 = "(" 
    part2 = str(getpass.getuser()) + "@" + str(os.path.basename(os.getcwd()))
    part3 = ")"
    part5 = hostname
    part6 =" | "
    part7 = now
    part8 = ")" + "\n"
    new_str = part1 + part2 + part3 + part5 + part6 + part7 + part8
    width = noOfColumns - len(new_str) -1
    part4 = "(".rjust(width, "-")
    part13 = "$ "

input_required = [
    ('class:parantheses1', part1),
    ('class:username', part2),
    ('class:parantheses2', part3),
    ('class:parantheses3', part4),
    ('class:hostname', part5),
    ('class:pipe', part6),
    ('class:date-time', part7),
    ('class:parantheses4', part8),
    ('class:parantheses5', part9),
    ('class:git-branch', part10),
    ('class:star', part11),
    ('class:parantheses6', part12),
    ('class:end', part13)
]

