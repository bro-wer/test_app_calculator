import sys

def ValidateArgsCount():
    if len(sys.argv) != 4:
        raise Exception("Unexpected args count!")

def ValidateArgs():
    try:
        CheckIfInt(sys.argv[1])
        CheckIfInt(sys.argv[2])
        CheckIfValidEquation(sys.argv[3])
    except Exception as e:
        raise e

def CheckIfInt(var):
    try:
        temp = int(var)
    except Exception as e:
        raise Exception("Provided variables are not int types!")

def CheckIfValidEquation(var):
    validEquationTypes = ["+", "-", "*" ,"/"]
    if not var in validEquationTypes:
        raise Exception("Provided equation type is not valid!")

def CalculateEquation():
    firstArg = int(sys.argv[1])
    secondArg = int(sys.argv[2])
    equation = sys.argv[3]
    result = eval("{}{}{}".format(firstArg, "+", secondArg))
    print(result)


if __name__ == '__main__':
    try:
        ValidateArgsCount()
        ValidateArgs()
        CalculateEquation()
    except Exception as e:
        print(e)
