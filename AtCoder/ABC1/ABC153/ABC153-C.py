n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
use_sp = min(k, len(h))
for _ in range(use_sp): h.pop()
print(sum(h))