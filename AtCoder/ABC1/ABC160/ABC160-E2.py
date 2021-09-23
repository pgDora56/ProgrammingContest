import heapq

x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p2 = heapq.nlargest(x, p)
q2 = heapq.nlargest(y, q)
r2 = heapq.nlargest(x+y, r)
p2.append(0)
q2.append(0)
r2.append(0)

pi = 0
qi = 0
ri = 0

val = 0

for _ in range(x+y):
    if p2[pi] >= q2[qi] and p2[pi] >= r2[ri]:
        val += p2[pi]
        pi += 1
    elif p2[pi] <= q2[qi] and q2[qi] >= r2[ri]:
        val += q2[qi]
        qi += 1
    else:
        val += r2[ri]
        ri += 1

print(val)
