def isPrime(n):
    i = 2
    if n % 2 == 0:
        return False
    while i  <= (n / 2):
        if n % i == 0:
            return False
        i += 1
    return True
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors


pfs = prime_factors(1000)
largest_prime_factor = max(pfs)

print(prime_factors(600851475143))
print(primeFactor(int(input("What do you want to check? "))))
