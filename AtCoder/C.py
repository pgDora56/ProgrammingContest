def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

n = int(input())
a = list(map(int, input().split()))

f = [0]
b = [0]

for i in range(n):
    f.append(gcd(f[i], a[i]))
    b.append(gcd(b[i], a[n-1-i]))

b.reverse()
ans = []
for i in range(n-1):
    ans.append(gcd(f[i], b[i+1]))
print(max(ans))