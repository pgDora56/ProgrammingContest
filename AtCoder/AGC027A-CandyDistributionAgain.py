n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in a:
    if x - i >= 0:
        x -= i
        count += 1
    else:
        x = 0
        break
if x != 0: count -= 1
print(count)