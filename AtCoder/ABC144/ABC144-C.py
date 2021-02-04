from math import sqrt, floor
n = int(input())
for i in range(floor(sqrt(n)), 0, -1):
    if n % i == 0:
        j = n // i
        print(i+j-2)
        exit()
