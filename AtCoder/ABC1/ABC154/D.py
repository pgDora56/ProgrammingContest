from collections import deque
n,k = map(int,input().split())
p = list(map(int,input().split()))
s = deque()
s.append(0)
tot = 0
for i in p:
    tot += i
    s.append(tot)

top = 0
for i in range(n-k+1):
    top = max(top, s[i+k]-s[i])

print((top+k)/2)
