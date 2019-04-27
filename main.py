import sys

if __name__ == '__main__':
    print ("This is the name of the script: ", sys.argv[0])
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))
    firstArg = sys.argv[1]
    secondArg = sys.argv[2]
    equation = sys.argv[3]
    print(firstArg + secondArg)
