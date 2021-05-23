def repl(command) -> None:
    try:
        print(eval(command))
    except:
        out = exec(command)
        if out != None:
            print(out)  