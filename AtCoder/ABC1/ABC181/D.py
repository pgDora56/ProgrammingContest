lis = [0] * 9
s = input()
if len(s) < 3:
    v = int(s)
    if v % 8 == 0:
        print("Yes")
        exit()
    if ((v % 10) * 10 + (v // 10)) % 8 == 0:
        print("Yes")
        exit()
    print("No")
    exit()

for c in s:
    lis[int(c)-1] += 1

req = [0] * 9
for h in range(9):
    req[h] += 1
    for t in range(9):
        req[t] += 1
        for o in range(9):
            req[o] += 1
            ok = True
            for v in [h, t, o]:
                if req[v] > lis[v]:
                    ok = False
                    break
            if ok:
                val = (h + 1) * 100 + (t + 1) * 10 + o + 1
                if val % 8 == 0:
                    print("Yes")
                    exit()
            req[o] -= 1
        req[t] -= 1
    req[h] -= 1

print("No")
