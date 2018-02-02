#Count 1 to 10
def count():
    for i in range(1,11):
        print(i)
#Count User prompt
def countUser(start,end):
    for i in range(start,end+1):
        print(i)
#countUser(int(input("Start From: ")),int(input("End on: ")))
#Count Odd Numbers
def CountOdd(start,end):
    if (start%2==0):
        start+=1
    for i in range(start,end,2):
        print(i)
#Coin counting
def coinCounting():
    coins=0
    def getCoin():
        userInput=input("Do you want a coin(Yes/No) ").upper()
        if userInput == "YES":
            return 1
        elif userInput == "NO":
            return 0
        else:
            print(f"Whoops, {userInput} is not a vaild input please use only yes or no.")
            return getCoin()
    while True:
        print(f"You have {coins} coins.")
        if getCoin() == 1:
            coins+=1
        else:
            break
#coin()
#Print a Square
def printASquare(rowEnd,columnEnd):
    row=0
    column=0
    while column<=columnEnd:
        while row<=rowEnd:
            print("* ",end="")
            row+=1
        print()
        row=0
        column+=1
#printASquare((int(input("How many rows do you want? "))-1),(int(input("How many columns do you want? "))-1))
#Print a Box
def printABox(rowEnd,columnEnd):
    row = 0
    column = 0
    while column<=columnEnd:
        while row<=rowEnd:
            if column == 0 or column == columnEnd:
                print("* ",end="")
            elif row == 0 or row == rowEnd:
                print("* ",end="")
            else:
                print("  ",end="")
            row+=1
        print()
        row=0
        column+=1
#printABox((int(input("How many rows do you want? "))-1),(int(input("How many columns do you want? "))-1))
#Prints a Trangle
def printATriangle(height):
    def nthOdd(number):
        return (2 * number) - 1
    rowBase = nthOdd(height)
    row = 1
    while height > 0:
        stars = nthOdd(row)
        spaces = (rowBase - stars) // 2
        print(("  " * spaces) + ("* " * stars) + ("  " * spaces))
        row+=1
        height-=1
#printATriangle(int(input("How Hight do you want the triangle? ")))

def triangleNumbers(nMax):
    visual=input("Do you want to print each triangle?(Y/N) ").upper()
    n=1
    while n <= nMax:
        print(f"{n}: {(n*(n+1)/2)}")
        if visual == "Y":
            printATriangle(n)
        n+=1

#triangleNumbers(int(input("How many trinagle numbers should be generated? ")))
def printABanner(textList):
    row = 0
    column = 0
    high = len(1)
    for i in textList:
        if len(i) > high:
            high = len(i)
    rowEnd =  high + 2
    columnEnd = len(textList) + 1
    while column<=columnEnd:
        while row<=rowEnd:
            #print(row, end="")
            #print(column,end="")
            if column == 0 or column == columnEnd:
                print("* ",end = "")
            elif row == 0 or row == rowEnd:
                print("* ",end = "")
            elif (row - 1) < len(textList[column-1]):
                print(f"{textList[column-1][row-1]} ",end = "")
            else:
                print("  ",end = "")
            row+=1
        print()
        row=0
        column+=1
print("""Please type your banner text hit enter for a new line.
Type end on it's own line to terimate text entry""")
textList = []
# while True:
#     userInput = input(": ")
#     if userInput.upper() == "END":
#         break
#     else:
#         textList.append(userInput)
# printABanner(textList)

def multiTable(start,end):
    for i in range(start,end+1):
        for n in range(start,end+1):
            print(f"{i} * {n} = {i * n}")
#multiTable(int(input("Starting number? ")),int(input("Ending number? ")))
def factor(number):
    output=[]
    for i in range(1,number+1):
        if number % i == 0:
            output.append(i)
    return output
print(factor(int(input("What number do you want factored?"))))
