w,h,x,y = map(int, input().split())
mult = 1 if w / 2 == x and h / 2 == y else 0
print("{} {}".format(w*h/2, mult))