import math, decimal

memo = [1,2,4,8,16,32,64,128,256,512,1024,2048]
def twopow(f):
    if len(memo) < f:
        return memo[f]
    else:
        repeat = f - len(memo) + 1
        for _ in range(repeat):
            memo.append(memo[len(memo)-1]*2)
        return memo[f]

n, k = map(int,input().split())
per = 0
for i in range(1, n+1):
    x = math.ceil(math.log2(k/i)) if k > i else 0
    # x = 0
    # t = i
    # while t < k:
    #     t *= 2
    #     x += 1
    # per += float("{:.20g}".format(1/(2**x)))
    per += 2**-x

print(per/n)