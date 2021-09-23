# Not solve
n = int(input())
a = list(map(int, input().split()))

total = 0
for i in range(len(a)):
    if i < a[i]:
        total += a[i] - i
print(total)
