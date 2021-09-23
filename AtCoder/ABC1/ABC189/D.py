n = int(input())
ans = 1
for i in range(n):
    s = input()
    if s == "OR":
        ans += 2 << i
print(ans)
