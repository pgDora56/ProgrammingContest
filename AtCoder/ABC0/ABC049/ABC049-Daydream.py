s = list(input())
erOK = False
while len(s) > 1:
    if len(s) > 4:
        if s[0] == "d":
            if s[1] == "r" and s[2] == "e" and s[3] == "a" and s[4] == "m":
                del s[0:5]
                erOK = True
                continue
        elif s[0] == "e":
            if s[1] == "r" and s[2] == "a" and s[3] == "s" and s[4] == "e":
                del s[0:5]
                if len(s) > 0:
                    if s[0] == "r": del s[0]
                continue
    if erOK and s[0] == "e" and s[1] == "r":
        del s[0:2]
        erOK = False
        continue
    break
if len(s) == 0: print("YES")
else: print("NO")
