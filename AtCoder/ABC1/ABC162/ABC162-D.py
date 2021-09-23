n = int(input())
s = input()
cnt = s.count("R") * s.count("G") * s.count("B")
for i in range(n-2):
    pl = 1
    while i + pl * 2 < n:
        if s[i] != s[i+pl] and s[i+pl] != s[i+pl*2] and s[i] != s[i+pl*2]:
            cnt -= 1
        pl += 1
print(cnt)
