n = int(input())
a = list(map(int,input().split()))
b = []
total = sum(a)
for i in range(1, n, 2):
    total -= a[i] * 2
b.append(total)
prev = total
for i in a:
    prev = 2 * i - prev
    b.append(prev)

result = ""
for i in range(n):
    if i != 0: result += " "
    result += str(b[i])
print(result)
