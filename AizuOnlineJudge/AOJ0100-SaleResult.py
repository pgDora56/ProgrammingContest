while True:
    n = int(input())
    if n == 0: break
    dic = {}
    for i in range(n):
        e, p, q = map(int, input().split())
        if e in dic:
            dic[e] += p * q
        else:
            dic[e] = p * q
    flag = False
    for p in dic:
        if dic[p] >= 1000000:
            print(p)
            flag = True
    if not flag:
        print("NA")