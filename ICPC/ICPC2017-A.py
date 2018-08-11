import itertools
while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0): break
    a = list(map(int, input().split()))
    ans = -1
    for combi in itertools.combinations(a, 2):
        if combi[0] + combi[1] <= m: ans = max(ans, combi[0] + combi[1])
    if ans == -1: print("NONE")
    else: print(ans)
