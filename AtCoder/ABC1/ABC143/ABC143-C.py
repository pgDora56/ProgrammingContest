n = int(input())
s = input()

prev = ""
cnt = 0
for c in s:
    if prev != c:
        cnt += 1
        prev = c
print(cnt)
