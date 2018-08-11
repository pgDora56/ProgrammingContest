while True:
    try:
        a,b,c,d,e,f = map(int, input().split())
        y = (a * f - c * d) /  (a * e - b * d)
        if a != 0: x = (c - b * y) / a
        else: x = (f - e * y) / d
        print("{:.3f} {:.3f}".format(round(x, 3), round(y, 3)))
    except: break
