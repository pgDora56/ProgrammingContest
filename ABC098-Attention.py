# TLE
n = int(input())
s = input()
check = set([0, n-1])
for i in range(n-1):
    if s[i] != s[i+1]: check = check | set([i, i+1])
ans = n
for i in check:
    tmp = 0
    for j in range(0, i):
        if s[j] == "W": tmp += 1
    for k in range(i+1, n):
        if s[k] == "E": tmp += 1
    ans = min(ans, tmp)
print(ans)