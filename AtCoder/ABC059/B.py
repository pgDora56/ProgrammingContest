a = input()
b = input()
la = len(a)
lb = len(b)
if la < lb:
    print("LESS")
elif la > lb:
    print("GREATER")
else:
    cas = list(a)
    cbs = list(b)
    for i in range(la):
        if int(cas[i]) > int(cbs[i]):
            print("GREATER")
            exit()
        elif int(cas[i]) < int(cbs[i]):
            print("LESS")
            exit()
    print("EQUAL")


