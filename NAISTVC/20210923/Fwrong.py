H, W = map(int, input().split())

orbs = []
ingots = [0] * W
jewels = []

for hs in range(H):
    x = input()
    orb_cnt = 0
    for ws in range(W):
        v = x[ws]
        if v == "J":
            jewels.append((hs, ws))
        elif v == "O":
            orb_cnt += 1
        else:
            ingots[ws] += 1
    orbs.append(orb_cnt)

print(orbs)
print(ingots)
total = 0
for j in jewels:
    total += orbs[j[0]] * ingots[j[0]]
    print(j, orbs[j[0]], ingots[j[0]], total)
print(total)

# ~~~~~~~~
H, W = map(int, input().split())

orbs = []
ingots = [0] * W
jewels = []

for hs in range(H):
    x = input()
    orb_cnt = 0
    for ws in range(W):
        v = x[ws]
        if v == "J":
            jewels.append((hs, ws, orb_cnt, ingots[ws]))
        elif v == "O":
            orb_cnt += 1
        else:
            ingots[ws] += 1
    orbs.append(orb_cnt)

total = 0
for j in jewels:
    total += (orbs[j[0]] - j[2]) * (ingots[j[1]] - j[3])
print(total)
