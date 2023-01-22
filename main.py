import subprocess


def getinput():
    return input()


def main():
    while True:
        getinput()
        if "code" in getinput:
            subprocess.Popen("")


if __name__ == '__main__':
    main()
