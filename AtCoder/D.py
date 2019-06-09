n = int(input())
a = list(map(int, input().split()))
total = 0
minus = 0
smallest = abs(a[0])
for i in range(n):
    smallest = min(smallest, abs(a[i]))
    if a[i] < 0:
        minus = (minus + 1) % 2
        total -= a[i]
    else:
        total += a[i]
if minus == 1:
    print(total - 2 * smallest)
else:
    print(total)