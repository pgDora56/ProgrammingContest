while True:
    n = int(input())
    if n == 0: break
    dic = {}
    for i in range(n):
        f, t  = input().split()
        dic[f] = t
    print(dic)
    n = int(input())
    op = ""
    for i in range(n):
        l = input()
        if l in dic: op += dic[l]
        else: op += l
    print(op.replace("\t", "").replace(" ",""))
