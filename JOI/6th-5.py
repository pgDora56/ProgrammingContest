a, b, c = map(int, input().split())
n = int(input())
check = [2 for _ in range(a+b+c)]
bad = []
for _ in range(n):
    i,j,k,r = map(int, input().split())
    if r == 0: bad.append([i-1,j-1,k-1])
    else:
        check[i-1] = 1
        check[j-1] = 1
        check[k-1] = 1
while len(bad) != 0:
    delete = []
    for b in range(len(bad)):
        x = bad[b]
        if 0 in x:
            delete.append(b)
        elif check[x[0]] == 1 and check[x[1]] == 1:
            check[x[2]] = 0
            delete.append(b)
        elif check[x[1]] == 1 and check[x[2]] == 1:
            check[x[0]] = 0
            delete.append(b)
        elif check[x[0]] == 1 and check[x[2]] == 1:
            check[x[1]] = 0
            delete.append(b)
    if len(delete) == 0:
        break
    else:
        delete.sort(reverse = True)

        for d in delete:
            bad.pop(d)

for v in check:
    print(v)
