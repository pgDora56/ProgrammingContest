n, m = map(int,input().split())
if m < 2*n or 4*n < m:
    print("-1 -1 -1")
else:
    dist = m - 2*n
    o = dist % 2
    b = (dist-o) // 2
    a = n - o - b
    print(a,o,b)

