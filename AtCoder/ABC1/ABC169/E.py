n = int(input())
a = []
b = []
for _ in range(n):
    ae, be = map(int,input().split())
    a.append(ae)
    b.append(be)
a.sort()
b.sort()

center = n // 2
if n % 2 == 0:
    st = a[center] + a[center-1]
    en = b[center] + b[center-1]
    print(en-st+1)
else:
    print(b[center]-a[center]+1)
