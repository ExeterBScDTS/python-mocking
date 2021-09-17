from myimport import anotherfunction


def myfunction(arg1, arg2):

    results = []

    results.append(anotherfunction(arg1))
    results.append(anotherfunction(arg2))

    return results


if __name__ == "__main__":
    myfunction(1, 2)
