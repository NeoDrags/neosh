import subprocess
from prompt_toolkit.styles import Style
from pathlib import Path
from socket import gethostname
import os
import getpass

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
hostname = gethostname()
history = Path(HOME_DIR + "/.yash_history")

x = subprocess.getoutput("git rev-parse --is-inside-work-tree")

part1 =""
part2 =""
part3 =""

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

