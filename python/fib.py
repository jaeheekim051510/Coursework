def fibEven(maxFib):
    fib = [1]
    sums = 0
    n = 0
    i = 0
    while n < maxFib:
        n = fib[i] + fib[i-1]
        if n % 2 == 0 and n < maxFib:
            sums += n
        fib.append(n)
        i += 1
    return sums
print(fibEven(4000000))
