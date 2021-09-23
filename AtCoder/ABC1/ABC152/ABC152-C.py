n = int(input())
p = list(map(int,input().split()))

ok = n + 1
cnt = 0
for i in p:
    if i <= ok:
        cnt += 1
        ok = i
print(cnt)

