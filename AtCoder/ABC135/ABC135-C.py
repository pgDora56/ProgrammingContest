n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

count = 0
if b[0] >= a[0]:
    count = a[0]
    b[0] -= a[0]
else:
    count = b[0]
    b[0] = 0
    
for i in range(1, n):
    if a[i]==0: continue
    if b[i-1] >= a[i]:
        count += a[i]
        continue
    if b[i] >= a[i] - b[i-1]:
        count += a[i]
        b[i] -= (a[i] - b[i-1])
        continue
    count += b[i-1] + b[i]
    b[i] = 0

count += min(a[-1], b[-1])

print(count)
    

