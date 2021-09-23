# 切断点を求めればいけそう
n = int(input())
path = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
