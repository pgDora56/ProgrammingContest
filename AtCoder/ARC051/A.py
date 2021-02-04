rx, ry, r = map(int,input().split())
bx1, by1, bx2, by2 = map(int,input().split())

if bx1 <= rx - r and rx + r <= bx2 and by1 <= ry - r and ry + r <= by2:
    print("NO")
else:
    print("YES")

for x in [bx1, bx2]:
    for y in [by1, by2]:
        if pow(x-rx,2) + pow(y-ry,2) > pow(r,2):
            print("YES")
            exit()
print("NO")
