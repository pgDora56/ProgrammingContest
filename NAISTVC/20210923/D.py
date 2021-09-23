import math
n = int(input())
nam = input()
nam_l = len(nam)

ans = 0

for _ in range(n):
    sign = input()
    for st in range(len(sign) - nam_l + 1):
        if sign[st] != nam[0]:
            continue

        maxi_dist = math.ceil((len(sign)-st)/(nam_l-1))
        for dist in range(1, maxi_dist):
            for idx in range(nam_l):
                if sign[st+dist*idx] != nam[idx]:
                    break
            else:
                ans += 1
                break
        else:
            continue
        break

print(ans)
