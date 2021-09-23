w,h,n=map(int,input().split())
xmin, xmax, ymin, ymax = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        if x > xmin:
            xmin = x
    elif a == 2:
        if x < xmax:
            xmax = x
    elif a == 3:
        if y > ymin:
            ymin = y
    else:
        if y < ymax:
            ymax = y

if xmax-xmin < 0 or ymax-ymin < 0:
    print(0)
    exit()
ans = (xmax-xmin) * (ymax-ymin)
print(ans)
