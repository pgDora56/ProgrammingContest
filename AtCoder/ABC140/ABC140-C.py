n = int(input())
b = list(map(int,input().split()))

a = [b[0]]

for i in b:
    if a[-1] > i: a[-1] = i
    a.append(i)
print(sum(a))
