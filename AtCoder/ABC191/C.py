h, w = map(int, input().split())
total = 0
prev = input()
for _ in range(h-1):
    now = input()
    for x in range(w-1):
        cnt = 0
        if prev[x] == "#":
            cnt += 1
        if prev[x+1] == "#":
            cnt += 1
        if now[x] == "#":
            cnt += 1
        if now[x+1] == "#":
            cnt += 1
        if cnt % 2 == 1:
            total += 1
    prev = now
print(total)
