x,n = map(int,input().split())
p = list(map(int,input().split()))
flag = [True] * 102

for i in p:
    flag[i] = False

for i in range(101):
    low = max(x-i, 0)
    high = min(x+i, 101)
    if flag[low]:
        print(low)
        break
    elif flag[high]:
        print(high)
        break
