s = input()
t = input()

s2 = []
t2 = []

sdic = {}
tdic = {}

cnt = 0
for c in s:
    if c in sdic:
        s2.append(sdic[c])
    else:
        s2.append(cnt)
        sdic[c] = cnt
        cnt += 1

cnt = 0
for c in t:
    if c in tdic:
        t2.append(tdic[c])
    else:
        t2.append(cnt)
        tdic[c] = cnt
        cnt += 1
        
print(s2)
print(t2)

print("Yes" if s2 == t2 else "No")
