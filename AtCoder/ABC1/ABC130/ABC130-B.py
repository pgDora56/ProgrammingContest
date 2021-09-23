n, x = map(int, input().split())
l = list(map(int,input().split()))
count = 1
d = 0
for lx in l:
    d += lx
    if d <= x: 
        count += 1
    else: break
print(count)