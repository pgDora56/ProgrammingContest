n, m, x = map(int,input().split())
books = []
for _ in range(n):
    books.append(list(map(int,input().split())))
price = float('inf')

for i in range(2**n):
    prtmp = 0
    skill = [0] * m
    for j in range(n):
        if i >> j & 1:
            prtmp += books[j][0]
            for s in range(m):
                skill[s] += books[j][s+1]
    clear = True
    for s in skill:
        if s < x:
            clear = False
            break
    if clear:
        price = min(price,prtmp)

print(-1 if price == float('inf') else price)
