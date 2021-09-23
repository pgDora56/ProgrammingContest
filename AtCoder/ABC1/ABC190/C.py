n, m = map(int,input().split())
conds = []
people = []
for _ in range(m):
    conds.append(list(map(lambda x:int(x)-1,input().split())))
k = int(input())
for _ in range(k):
    people.append(list(map(lambda x:int(x)-1,input().split())))

maxi = 0
for bits in range(2**k):
    ball = [False] * n
    cnt = 0
    for i in range(k):
        if bits>>i & 1:
            ball[people[i][0]] = True
        else:
            ball[people[i][1]] = True
    for c in conds:
        if ball[c[0]] and ball[c[1]]:
            cnt += 1
    maxi = max(maxi,cnt)
print(maxi)

