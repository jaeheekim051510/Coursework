#isLower is built into python😦
import Terry
def reverse(input):
    output=""
    for i in range(len(input)-1,-1,-1):
        output+=input[i]
    return output
#print(reverse("test"))
def leetspeak(input):
    translationDict = {
        "A":"4",
        "E":"3",
        "G":"6",
        "I":"1",
        "O":"0",
        "S":"5",
        "T":"7"
        }
    output=""
    for i in range(len(input)):
        if (input[i].upper()) in translationDict:
            output+=translationDict[input[i].upper()]
        else:
            output+=input[i]
    return output
#print(leetspeak("leet"))
def longVowels(input):
    vowel = ["A","E","I","O","U"]
    output = ""
    i = 0
    while i < len(input):
        print(i)
        if input[i].upper() in vowel:
            if i < (len(input ) - 1):
                if input[i + 1].upper() == input[i].upper():
                    output+=(input[i]*5)
                    i += 2
                else:
                    output += input[i]
                    i += 1
            else:
                output += input[i]
                i += 1
        else:
            output += input[i]
            i += 1
    return output
#print(longVowels("GOod"))
def rot13(input):
    output = ""
    temp = ""
    for i in range(len(input)):
        if Terry.isLetter(input[i]):
            case = Terry.getCase(input[i])
            temp = ord(input[i]) + 13
            if temp > 90 and case == "upper":
                temp -= 26
            elif temp > 122 and case == "lower":
                temp -= 26
                output += chr(temp)
        else:
            output += input[i]
    return output
print(rot13("This is a Test of 0ther character support🚁😀"))
