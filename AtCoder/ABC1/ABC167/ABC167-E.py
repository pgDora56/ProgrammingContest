fac = [1,1]
def factorial(n):
    global CONST
    while len(fac) <= n:
        fac.append(fac[-1] * len(fac) % CONST)
    return fac[n]

CONST = 998244353
n,m,k = map(int,input().split())
total = 0
for i in range(k+1):
    block = m * (pow(m-1, n-i-1, CONST)) % CONST
    db = factorial(n)
    db2 =  (factorial(i)) 
    db2 = db2 * (factorial(n-i)) 
    db //= db2
    total = (total+block*db%CONST)%CONST

print(int(total))
