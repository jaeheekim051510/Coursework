n = 1000
sums = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sums += i
print(sums)
