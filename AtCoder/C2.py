from collections import deque

CONST = 1000000007

n,m = map(int,input().split())
lis = deque([int(input()) for _ in range(m)])
lis.append(n+1)
nhole = lis.popleft()

memo = deque([0, 1])
for i in range(1,n+1):
    if i == nhole:
        memo.append(0)
        nhole = lis.popleft()
    else:
        memo.append((memo[-1] + memo[-2])%CONST)
print(memo[-1])

