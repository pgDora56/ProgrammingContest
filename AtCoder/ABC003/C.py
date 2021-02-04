n, k = map(int,input().split())
r = list(map(int,input().split()))
r.sort(reverse=True)
div = 2
rate = 0
for i in range(k):
    rate += r[i] / div
    div *= 2
print(rate)
