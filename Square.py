def printLine(xDimension,columns):
    for a in range (0,columns):
        print ('+', end = ' ')
        for b in range (0,xDimension):
            print ('-', end = ' ')
    print ('+')


def printSection(xDimension,columns):
    for a in range (-1,columns):
        print ('/', end = ' ')
        for b in range (0,xDimension):
            print ('  ', end = '')
    print ("")


def printPicture(xDimesionInput,rowsInput,columnsInput):
    for a in range (0,rowsInput):
        printLine(xDimesionInput,columnsInput)
        for b in range (0,xDimesionInput):
            printSection(xDimesionInput,columnsInput)
    printLine(xDimesionInput,columnsInput)

x = input("Square Dimensions?: ")
y = input("Rows?: ")
z = input("Columns?: ")
intX = int(x)
intY= int(y)
intZ = int(z)
printPicture(intX,intY,intZ)
