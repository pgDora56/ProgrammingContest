input()
an = list(map(int, input().split()))
count = 0
for a in an:
    while a % 2 == 0:
        a /= 2
        count += 1
print(count)