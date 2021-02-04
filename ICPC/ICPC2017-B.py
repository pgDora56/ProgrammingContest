while True:
    a = input()
    if a == ".": break
    b = input()
    if a == b: print("IDENTICAL")
    else:
        a2 = a.split('"')
        b2 = b.split('"')
        if len(a2) != len(b2):
            print("DIFFERENT")
            continue
        l = min(len(a2), len(b2))
        is_close = True
        close_count = 0
        for i in range(0,l):
            if i % 2 == 0:
                if a2[i] != b2[i]:
                    is_close = False
                    break
            else:
                if a2[i] != b2[i]:
                    close_count += 1
                if close_count > 1:
                    is_close = False
                    break
        if is_close: print("CLOSE")
        else: print("DIFFERENT")