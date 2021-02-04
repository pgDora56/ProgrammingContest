n, m = map(int, input().split())
num = ["n"] * n
for _ in range(m):
    s,c = map(int,input().split())
    if not(num[s-1] == "n" or num[s-1] == str(c)) or (n != 1 and s == 1 and c == 0):
        print(-1)
        exit()
    else:
        num[s-1] = str(c)

op = ""
for ns in range(len(num)):
    if num[ns] == "n": 
        if ns == 0 and n != 1 : op += "1"
        else: op += "0"
    else: op += num[ns]
print(op)
