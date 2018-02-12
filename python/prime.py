#! /usr/bin/env python3

import math
import sys

def isPrime(n):
    a = 2
    b = -1
    while n % 2 == 0:
        return False
    while a < n:
        b = math.sqrt(abs((a ** 2)-n))
        if b.is_integer() and a + b > 1 and a - b > 1:
            c = abs(a - b)
            d = abs(a + b)
            if c * d == n:
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
    print(a,n2)
    while abs(a + b) < n:
        print(a)
        b = math.sqrt(abs((a ** 2)-n2))
        if b.is_integer():
            c = abs(a - b)
            d = abs(a + b)
            if c not in factors:
                if c % 2 != 0:
                    factors.append(c)
                if d % 2 != 0:
                    factors.append(d)
            print(a,b)
        a += 1
    print(factors)
    for i in factors:
        if isPrime(i):
            return i
    return n

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if '--test-prime' in sys.argv:
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
        if '--test-largestPrime' in sys.argv:
            fail = False

    else:
        print(largestPrime(int(input("What number do you want tested? "))))
