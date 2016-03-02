import time

def delayedPrint(string, delay):

    
    for l in string:
        if l == "\\" and string[string.index(l)+1] == "n":
            print("\n")
        elif l == "n" and string[string.index(l)-1] == "\\":
            pass
        else:
            print(l, end="")
        time.sleep(delay)

def dialogue(name, string, delay):
    print("{0}: ".format(name), end="")
    delayedPrint(string, delay)


dialogue("JOSH", "Ayy lmao", 0.3)