s = input()

cnt = 0
ans = 0

for c in s:
    if c == "B":
        cnt += 1
    else:
        ans += cnt
print(ans)
