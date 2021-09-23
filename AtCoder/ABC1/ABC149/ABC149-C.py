from math import sqrt, floor
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, floor(sqrt(n))+1, 2):
        if n % i == 0: return False
    return True

val = (lambda x: x if x % 2 != 0 or x == 2 else x + 1)(int(input()))

for i in range(val, val * 2 + 1):
    if is_prime(i):
        print(i)
        exit()

