import math
def is_prime(val):
    if val % 2 == 0: return False
    for i in range(3, int(math.sqrt(val))+1, 2):
        if val % i == 0: return False
    return True

while True:
    n, p = map(int,input().split())
    if n == -1 and p == -1: break
    
    