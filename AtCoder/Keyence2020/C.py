n, k, s = map(int,input().split())
snext = s + 1
if s == 10**9:
    snext = 1
a = []
for i in range(n):
    if i < k:
        a.append(str(s))
    else:
        a.append(str(snext))
print(" ".join(a))
