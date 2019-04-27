import sys

def ValidateArgsCount():
    if len(sys.argv) != 4:
        raise Exception("Unexpected args count!")

def CalculateEquation():
    firstArg = sys.argv[1]
    secondArg = sys.argv[2]
    equation = sys.argv[3]
    print(firstArg + secondArg)


if __name__ == '__main__':
    try:
        ValidateArgsCount()
        CalculateEquation()
    except Exception as e:
        print(e)
