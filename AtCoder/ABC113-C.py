n, m = map(int,input().split())
cities = []
for i in range(m):
    p, y = map(int,input().split())
    cities.append([i,p,y,0])
cities.sort(key=lambda x: (x[2], x[1]))

pref = cities[0][1]
cnt = 1
for c in cities:
    if c[1] != pref:
        pref = c[1]
        cnt = 1
    c[3] = cnt
    cnt += 1

cities.sort(key=lambda x: x[0])
for c in cities:
    print(str(c[1]).zfill(6)+str(c[3]).zfill(6))

