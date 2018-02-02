py# phonebook_dict = {
#     'Alice' : '703-493-1834',
#     'Bob' : '857-384-1234',
#     'Elizabeth' : '484-584-2923'
# }
# print(phonebook_dict['Alice'])
# phonebook_dict['Kareem'] = '938-489-1234'
# phonebook_dict.pop('Alice')
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
# print(ramit['email'])
# print(ramit['interests'][0])
# for i in range(len(ramit['friends'])):
#     if ramit['friends'][i]['name'] == 'Jasmine':
#         print(ramit['friends'][i]['email'])
def isLetter(string):
    if len(string) > 1:
        raise TypeError("Get case excpeted a string of 1.")
    elif ord(string.lower()) >= 97 and ord(string.lower()) <= 122:
        return(True)
    else:
        return False
def letterSummary(input):
    countingDict = {}
    for i in range(len(input)):
        if isLetter(input[i]):
            if input[i].upper() in countingDict:
                countingDict[input[i].upper()] += 1
            else:
                countingDict[input[i].upper()] = 1
    return countingDict
#print(letterSummary("This is a test!"))
def wordSummary(input):
    words = input.split()
    countingDict = {}
    for i in range(len(words)):
            if words[i].lower() in countingDict:
                countingDict[words[i].lower()] += 1
            else:
                countingDict[words[i].lower()] = 1
    return countingDict
#print(wordSummary("This is a test of word summary!"))
