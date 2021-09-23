n, k = map(int, input().split())
mod = n % k
if abs(mod) > abs(mod-k):
    print(abs(mod-k))
else:
    print(mod)
