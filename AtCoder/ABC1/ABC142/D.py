def factorization(n,m):
    temp = n
    temp2 = m
    cnt=1
    for i in range(2, int(-(-min(n,m)**0.5//1))+1):
        if temp%i==0:
            if temp2%i == 0:
                cnt += 1
                while temp2%i==0:
                    temp2 //= i
            while temp%i==0:
                temp //= i
        elif temp2%i == 0:
            while temp2%i==0:
                temp2 //= i

    if temp != 1 and temp2 != 1:
        if max(temp, temp2) % min(temp, temp2) == 0: cnt += 1

    return cnt

a, b = map(int,input().split())
print(factorization(a,b))
