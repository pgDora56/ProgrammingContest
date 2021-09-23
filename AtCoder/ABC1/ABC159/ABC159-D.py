import math

n = int(input())
a = list(map(int,input().split()))

def combi(n):
    return math.factorial(n) // (math.factorial(n - 2) * 2)

a2 = sorted(a)
a2.append(n+1)
dic = {}
n = 0
cnt = 1
total = 0
for i in a2:
    if n != i:
        if cnt > 1:
            dic[str(n)] = cnt
            total += combi(cnt)
        n = i
        cnt = 1
    else:
        cnt += 1

for i in a:
    if str(i) in dic:
        cnt = dic[str(i)]
        print(total - cnt + 1)
    else:
        print(total)


