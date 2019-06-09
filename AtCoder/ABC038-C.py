n = int(input())
a = list(map(int, input().split()))
a.append(0)
prev = 10**6
count = 0
total = n
for v in a:
    if prev >= v:
        total += int(count*(count+1)/2)
        count = 0
    else:
        count += 1
    prev = v
print(total)