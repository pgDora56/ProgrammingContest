from collections import deque
n,m,k = map(int,input().split())
a = deque(map(int,input().split()))
b = deque(map(int,input().split()))
a2 = deque([0])
b2 = deque()

m = 0
for _ in range(len(a)):
    x = a.popleft()
    m += x
    if m > k:
        break
    a2.append(m)

m = 0
for _ in range(len(b)):
    x = b.popleft()
    m += x
    if m > k:
        break
    b2.append(m)

if len(a2) == 0:
    if len(b2) == 0:
        print(0)
        exit()
    else:
        print(len(b2))
elif len(b2) == 0:
    print(len(a2)-1)
    exit()

maxi = len(a2) - 1


ae = a2.pop()
be = b2.popleft()
books = len(a2)
while len(a2) > 0:
    if ae + be <= k:
        books += 1
        maxi = max(maxi, books)
        if len(b2) <= 0:
            break
        be = b2.popleft()
    else:
        books -= 1
        ae = a2.pop()
    
print(maxi)
