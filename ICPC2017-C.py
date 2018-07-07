while True:
    d, w = map(int, input().split())
    if (d, w) == (0, 0): break
    cells = [list(map(int, input().split())) for i in range(d)]
    for x in range(1, w - 2):
        for y in range(1, d - 2):
            for xd in range(1, w - 2 - x):
                for yd in range(1, d - 2 - y):
                    



