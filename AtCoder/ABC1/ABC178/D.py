import sys
import math
sys.setrecursionlimit(10**9)


def combi(n, ss):
    return (math.factorial(n) // (math.factorial(n-ss) * math.factorial(ss))) % mod


mod = 10**9 + 7

s = int(input())
if s < 3:
    print(0)
    exit()

ans = 1

size = 2
while size * 3 <= s:
    n = s - size * 2 - 1
    ss = size - 1
    ans = (ans + combi(n, ss)) % mod

    size += 1
print(ans)
