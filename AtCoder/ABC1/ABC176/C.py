n = int(input())
al = list(map(int,input().split()))
big = 0
total = 0
for a in al:
    if big > a:
        total += big - a
    else:
        big = a
print(total)
