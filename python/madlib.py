def extractString(stringInput, delimiter1, delimiter2):
    """Takes in a string, and delimiters and outputs the string with the text in
       between the delimiters remove and added to a list. Both the new string
       and the list are given in a tuple."""
    replacementPhrases = []
    finalString = ""
    mode =  0
    stringTemp = ""
    for index,letter in enumerate(stringInput):
        if letter == delimiter1:
            mode = 1
            finalString += value

        if letter == delimiter2:
            finalString += delimiter2
            mode = 0
            stringTemp += letter
            replacementPhrases.append(stringTemp)
            stringTemp = ""

        elif mode == 1:
            stringTemp += value

        elif mode == 0:
            finalString += value

        else:
            raise Exception("Extract string has failed!")
    print(finalString, replacementPhrases)
    return (phrases, finalString)


def madlib():
    print("""Beginning string entry. please type out the string with replacement
     points surrounded by curly brackets({}).
    Type end on it's own line to continue.""")
    stringTemp = ""
    stringFinal = """"""
    replacePhrases = []
    while stringTemp.upper() != "END":
        stringFinal += stringTemp + "\n"
        stringTemp = input()
    phrasesTuple = extractString(stringFinal,"{", "}")
    stringFinal = phrasesTuple[1]
    for i in phrasesTuple[0]:
        replacePhrases.append(input(f"What is {i}?"))
    print(replacePhrases)
    stringFinal.format(replacePhrases)
    print(stringFinal)
madlib()
