class Undefined(ArithmeticError):
    pass

def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum
#print(sum([1,2,3]))
def largestNumber(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
#print(largestNumber([1,2,3]))
def smallestNumber(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
#print(smallestNumber([1,2,3]))
def even(list):
    evens = []
    for i in list:
        if (i % 2 == 0):
            evens.append(i)
    return(evens)
#print(even([1,2,3,4]))
def positive(list):
    positives = []
    for i in list:
        if i > 0:
            positives.append(i)
    return positives
#print(positive([1,2,3,4]))
def multiplyList(list,factor):
    output = []
    for i in list:
        output.append(i*factor)
    return output
#print(multiplyList([1,2,3,4],2))
def multiplyVectors(list1,list2):
    output = []
    if len(list1) != len(list2):
        raise Undefined("multiplyVectors can not effect vectors of diffrent lengths!")
    for i in range(len(list1)):
        output.append(list1[i]*list2[i])
    return output
#print(multiplyVectors([1,2],[1,2]))
def addMatrix(list1,list2):
    rowTemp = []
    output = []
    #Error checkng variable
    rowMin = list1[0]
    #Error Checking protocl
    if len(list1) != len(list2):
        raise Undefined("Matrix additions can not be perfomred on matrices with diffrent bounds!")
    for i in list1:
        if len(i) != rowMin:
            raise Undefined("Matrix additions can not be perfomred on matrices with diffrent bounds!")
    for i in list2:
        if len(i) != rowMin:
            raise Undefined("Matrix additions can not be perfomred on matrices with diffrent bounds!")
    #Addition process
    for i in range(len(list1)):
        for n in range(len(list1[i])):
            rowTemp.append(list1[i][n] + list2[i][n])
        output.append(rowTemp)
    return output
print(addMatrix([[1,3],[2]],[[5,2],[1,0]]))
def deDup(list):
    output = []
    for i in list:
        if i not in output:
            output.append(i)
    return output
#print(deDup([1,2,3,1,"four","four","apple"]))
