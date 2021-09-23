from collections import deque
CONST = 10**9 + 7
n, k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

if k == 1:
    print(a[-1] % CONST)
    exit()

a2 = deque(a)

mini = a2.popleft()
maxi = a2.pop()

if maxi < 0 or mini > 0:
    a2.appendleft(mini)
    ans = maxi % CONST
    for i in range(k-1):
        ans = (ans * a2.pop()) %CONST
    print(ans)
    exit()


ans = 1
ans2 = 1
for i in range(k-1):
    if len(a2) == 0:
        ans2 = (ans2 * maxi) % CONST
        ans2 = (ans2 * mini) % CONST
        print(ans)
        exit()

    if abs(mini) < abs(maxi):
        ans *= maxi
        ans2 = ans2 * maxi % CONST
        maxi = a2.pop()
    else:
        ans *= mini
        ans2 = ans2 * mini % CONST
        mini = a2.popleft()
# print(ans, ans2, maxi, mini)
if ans * maxi < ans * mini:
    print((ans2*mini)%CONST)
else:
    print((ans2*maxi)%CONST)
