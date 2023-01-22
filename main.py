from location import *
from subprocess import Popen
from pymem import Pymem


def getinput():
    return input(">")


def checkIfRunning(a) -> str:
    try:
        Pymem(a+".exe")
    except:
        Popen(location[a])


def main():
    while True:
        inp = str(getinput())
        if "q" in inp or "exit" in inp:
            exit()
        if "explorer" in inp or "exp" in inp:
            Popen(location['explorer'], shell=True)
        if "vscode" in inp or "vs" in inp:
            Popen(location['vscode'], shell=True)
        if "notion" in inp or "no" in inp:
            Popen(location['notion'], shell=True)
        if "spotify" in inp or "sp" in inp:
            Popen(location['spotify'], shell=True)
        if ".code" in inp:
            checkIfRunning("vscode")
            checkIfRunning("opera")
            checkIfRunning("spotify")


if __name__ == '__main__':
    main()
