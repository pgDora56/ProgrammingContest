n, m = map(int, input().split())
a = list(map(int,input().split()))
total = sum(a)

count = 0
for i in range(n):
    if total <= a[i] * 4 * m:
        count += 1

if count >= m:
    print("Yes")
else:
    print("No")
