x, k, d = map(int,input().split())
if x < 0: x = -x
mv = x // d
if mv >= k:
    # なるべく0に近づけば良い
    print(abs(x)-d*k)
else:
    nearest = x % d
    if (k - mv) % 2 == 1:
        print(abs(nearest - d))
    else:
        print(nearest)
