import math
n = int(input())
f = 100
for i in range(1, math.floor(math.sqrt(n))+1):
    if n % i != 0: continue
    f = min(f, max(int(math.log10(i)+1), int(math.log10(n/i)+1)))
print(f)
