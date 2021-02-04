k = int(input())
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()

i = 7 % k
cnt = 1
while i != 0:
    i = i * 10 + 7
    i %= k
    cnt += 1
print(cnt)
