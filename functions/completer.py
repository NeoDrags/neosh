from prompt_toolkit.completion import Completer, Completion, merge_completers, WordCompleter
import glob

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

# class bashCommandCompleter(Completer):
#     def get_completions(self, document, complete_event):
#         word = document.get_word_before_cursor()
#         for command in merged_completers:
#             if command.startswith(word):
#                 yield Completion(
#                     command,
#                     start_position= -len(word)
#                 )

# class fileCompleter(Completer):
#     def get_completions(self, document, complete_event):
#         word = document.get_word_before_cursor()
#         for file in Files:
#             if file.startswith(word):
#                 yield Completion(
#                     file,
#                     start_position= -len(word)
#                 )
            

