while True:
    n = int(input())
    if n == 0: break
    at, bt = 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == b:
            at += a
            bt += b
        elif a > b:
            at += a + b
        else:
            bt += a + b
    print("{} {}".format(at,bt))
