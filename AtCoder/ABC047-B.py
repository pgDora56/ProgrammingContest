w,h,n=map(int,input().split())
xmin, xmax, ymin, ymax = 0, w, 0, h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        xmin = x
    elif a == 2:
        xmax = x
    elif a == 3:
        ymin = y
    else:
        ymax = y
ans = (xmax-xmin) * (ymax-ymin)
if ans < 0:
    print(0)
else:
    print(ans)
