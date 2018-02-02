import re
def extractString(string,delimiter1,delimiter2):
    index = 0
    index2 = 0
    output = []
    control = 0
    while True:
        index = string.find(delimiter1,index)
        control = string.find(delimiter1,index)
        if control == -1:
            break
        index2 = string.find(delimiter2,index) +1
        output.append([string[index:index2]])
        index += 1
    return output
def madlib():
    print("""Beginning string entry. please type out the string with replacement
     points surrounded by curly brackets({}).
    Type end on it's own line to continue.""")
    stringTemp = ""
    stringFinal = """"""
    replacePhrases = []
    while stringTemp.upper() != "END":
        stringTemp = input()
        if stringTemp.upper() != "END":
            stringFinal += stringTemp + "\n"
    phrases = extractString(stringFinal,"{","}")
    re.sub(r'{.+?}',stringFinal,'')
    print(stringFinal)
    for i in phrases:
        replacePhrases.append(input("What is {i}?"))
    stringFinal.format(phrases)
    print(stringFinal)
madlib()
