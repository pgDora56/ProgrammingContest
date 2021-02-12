import math

n = int(input())
cnt = 0
for i in range(1, math.floor(math.sqrt(n))+1):
    if n % i == 0:
        j = n // i
        if i == j:
            cnt += i % 2
        else:
            cnt += i % 2 + j % 2
print(cnt*2)
