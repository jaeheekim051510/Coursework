def isLetter(string):
    if len(string) > 1:
        raise TypeError("Get case excpeted a string of 1.")
    elif ord(string.lower()) >= 97 and ord(string.lower()) <= 122:
        return(True)
    else:
        return False
def getCase(string):
    if len(string) > 1:
        raise TypeError("Get case excpeted a string of 1.")
    elif ord(string) >= 97 and ord(string) <= 122:
        return("lower")
    elif ord(string) >= 65 and ord(string) <= 90:
        return("upper")
    else:
        raise TypeError("Get case excpeted a unicode alaphecitcal letter.")
class Undefined(ArithmeticError):
    pass
