n, m = map(int, input().split())
answered = [0] * n
ans = 0
pena = 0
for _ in range(m):
    p, s = input().split()
    pidx = int(p) - 1
    if answered[pidx] == -1:
        continue
    if s == "AC":
        ans += 1
        pena += answered[pidx]
        answered[pidx] = -1
    else:
        answered[pidx] += 1
print("{} {}".format(ans, pena))
