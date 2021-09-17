

def printlines():
    with open("myfile.txt") as myfile:
        for line in myfile:
            print(line)


if __name__ == "__main__":
    a = printlines()
    print(a)