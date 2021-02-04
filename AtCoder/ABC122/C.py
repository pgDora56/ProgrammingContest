n, q = map(int,input().split())
s = input()
querys = []
for _ in range(q):
    l, r = map(int,input().split())
    querys.append([l,r,0])

print(s[l-1:r].count("AC"))
