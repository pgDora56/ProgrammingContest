n,ye = map(int,input().split())
for x in range(n+1):
    if 10000 * x > ye: break
    for y in range(n-x+1):
        z = n - x - y
        tmp = 10000 * x + 5000 * y + 1000 * z
        if tmp == ye:
            print("{} {} {}".format(x,y,z))
            exit(0)
        elif tmp > ye:
            break
print("-1 -1 -1")
