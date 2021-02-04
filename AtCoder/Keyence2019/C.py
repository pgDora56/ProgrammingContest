n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

pos = []
neg = []
for i in range(n):
    d = a[i] - b[i]
    if d >= 0:
        pos.append(d)
    else:
        neg.append(-d)

pos.sort()


cnt = len(neg)
val = 0
while len(neg) > 0:
    n = neg.pop()
    while n > val:
        if len(pos) == 0:
            print(-1)
            exit()
        val += pos.pop()
        cnt += 1
    val -= n

print(cnt)

