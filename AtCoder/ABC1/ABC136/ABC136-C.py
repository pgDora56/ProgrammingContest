n = int(input())
h = list(map(int,input().split()))
h.reverse()

for i in range(1, len(h)):
    if h[i-1] >= h[i]: continue
    h[i] -= 1
    if h[i-1] < h[i]: 
        print("No")
        exit()
print("Yes")
