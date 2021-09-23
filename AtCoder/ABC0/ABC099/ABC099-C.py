n = int(input())

r = n

for i in range(n+1):
    cnt = 0
    nine = n - i
    while i > 0:
        cnt += i % 6
        i = i // 6
    while nine > 0:
        cnt += nine % 9
        nine = nine // 9
    if r > cnt: r = cnt

print(r)

