import math
def isPrime(n):
    a = 2
    b = -1
    while n % 2 == 0:
        return False
    while a + b < n :
        b = math.sqrt(abs((a ** 2)-n))
        if b.is_integer() and b > 1:
            return False
        a += 1
    return True
