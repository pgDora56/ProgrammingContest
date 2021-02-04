
Sd = input()
T  = input()
cand = []
lent = len(T)

for idx in range(len(Sd)-lent+1):
    p = 0
    while p < lent:
        if Sd[idx+p] != T[p] and Sd[idx+p] != "?":
            break

        if p == lent - 1:
            can = ""
            if idx > 0: can = Sd[:idx]
            can += T
            if idx + lent < len(Sd):
                can += Sd[(idx+lent):]
            cand.append(can.replace("?","a"))
        p += 1
if len(cand) == 0:
    print("UNRESTORABLE")
else: 
    cand.sort()
    print(cand[0])
