n = int(input())
for f in range(0, n + 1, 4):
    s = 0
    while f + s <= n:
        if f + s == n:
            print("Yes")
            exit(0)
        s += 7
print("No")