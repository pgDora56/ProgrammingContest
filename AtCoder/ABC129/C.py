import math
from collections import deque

memo = deque([1, 2])
floor = 1
def search(x):
    global memo, floor
    while x > floor:
        memo.append(memo[-1] + memo[-2])
        floor += 1
    return memo[x-1]

CONST = 1000000007
n,m = map(int,input().split())
lis = []
prev = -1
for _ in range(m):
    a = int(input())
    if prev + 1 == a:
        print(0)
        exit()
    lis.append(a-prev-2)
    prev = a
lis.append(n-prev-1)


ans = 1
for v in lis:
    if v == 0: continue
    ans = (ans * search(v)) % CONST
print(ans)

