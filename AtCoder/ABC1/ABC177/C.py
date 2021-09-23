CONST = 10**9 + 7
n = int(input())
a = list(map(int,input().split()))
s = pow(sum(a),2,CONST)
for x in a:
    s -= pow(x,2)
    s %= CONST
    if s < 0: s += CONST
print(s//2)
