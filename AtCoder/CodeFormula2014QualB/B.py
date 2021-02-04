n = input()

even = 0
odd = 0

nextEven = len(n) % 2 == 0

for c in n:
    if nextEven: even += int(c)
    else: odd += int(c)
    nextEven = not nextEven
print(even, odd)
