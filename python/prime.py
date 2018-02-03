#! /usr/bin/env python3

import math
import sys

def isPrime(n):
    a = 2
    b = -1
    while n % 2 == 0:
        return False
    while a + b < n:
        b = math.sqrt(abs((a ** 2)-n))
        if b.is_integer() and b > 1:
            return False
        a += 1
    return True

def largestPrime(n):
    factors = []
    n2 = n
    a = 2
    b = -1
    while n2 % 2 == 0:
        n2 /= 2
    factors.append(n2)
    while a + b < n :
        b = math.sqrt(abs((a ** 2)-n2))
        if b.is_integer():
            c = abs(a - b)
            d = abs(a + b)
            if c not in factors:
                if c % 2 != 0:
                    factors.append(c)
                if d % 2 != 0:
                    factors.append(d)
        a += 1
    for i in range(len(factors),0,-1):
        if isPrime(i):
            return i
    return n

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test-prime':
        fail = False
        for prime in [1, 3, 7, 13]:
            if not isPrime(prime):
                print("Fail: %d returned non-prime when it is" % (prime))
                fail = True
        for not_prime in [2, 4, 6, 15]:
            if isPrime(not_prime):
                print("Fail: %d returned prime when it is not" % (not_prime))
                fail = True
        if not fail:
            print("Prime test passed.")
    else:
        print(largestPrime(int(input("What number do you want tested? "))))
