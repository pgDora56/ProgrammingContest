sa = input()
sb = input()
sc = input()
turn = "a"
while True:
    if turn == "a":
        if len(sa)==0:
            print("A")
            exit(0)
        turn = sa[0]
        sa = sa[1:]
    elif turn == "b":
        if len(sb)==0:
            print("B")
            exit(0)
        turn = sb[0]
        sb = sb[1:]
    else:
        if len(sc)==0:
            print("C")
            exit(0)
        turn = sc[0]
        sc = sc[1:]
