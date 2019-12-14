# TLE
n, k = map(int, input().split())
a = list(map(int,input().split()))
su = [0]
cnt = 0
def check():
    global k, su, cnt
    l = len(su) - 1 - k 
    if l < 0: l = 0
    for i in range(l, len(su)-1):
        if (su[len(su)-1] - su[i]) % k == len(su) - 1 - i:
            cnt += 1

for i in a:
    su.append((su[len(su)-1]+i)%k)

    #su.append(su[len(su)-1]+i)
    #check()
print(cnt)

print(su)
