# 素因数分解
# nを与えて[2,4]のように素因数と指数のリストをリストにして返す
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

# 素数の列挙
def prime_numbers(n):
    prime = [2]
    for p in range(3, n, 2):
        for p2 in prime:
            if p % p2 == 0: break
        else: prime.append(p)
    return prime


# 最小公倍数の導出
# mathライブラリ必須, 3.4の場合はgcdはfractionsライブラリにあり
import math
def lcm(x, y):
    return (x * y) // math.gcd(x,y)
