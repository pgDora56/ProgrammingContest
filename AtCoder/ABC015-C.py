n, k = map(int, input().split())
t = []
for i in range(n):
    row = list(map(int, input().split()))
    if i == 0: 
        t = row
        continue
    newt = []
    for v in t:
        for r in row:
            newt.append(v^r)
    t = newt

if 0 in t:
    print("Found")
else:
    print("Nothing")
