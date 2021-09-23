n = int(input())
ipts = set(input() for _ in range(n))
for i in ipts:
    if "!" + i in ipts:
        print(i)
        exit()
print("satisfiable")
