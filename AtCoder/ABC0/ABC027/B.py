n = int(input())
a = list(map(int,input().split()))

if sum(a) % n != 0:
    print(-1)
    exit()

liveisland = sum(a) // n
s = 0
cnt = 0
bridge = 0
for ax in a:
    cnt += 1
    s += ax
    if cnt * liveisland == s:
        bridge += cnt - 1
        cnt = 0
        s = 0
print(bridge)

