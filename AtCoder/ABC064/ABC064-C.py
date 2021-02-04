n = int(input())
a = list(map(int, input().split()))
flag = [False for _ in range(8)]
flex = 0
for x in a:
    if x >= 3200:
        flex += 1
    else:
        flag[int(x/400)] = True
les = flag.count(True)
if les == 0 and flex > 0:
    print("1 {}".format(flex))
else:
    print("{} {}".format(les, les+flex))