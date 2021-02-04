n = int(input())
res = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}
for _ in range(n):
    res[input()] += 1
for k, v in res.items():
    print(f"{k} x {v}")
