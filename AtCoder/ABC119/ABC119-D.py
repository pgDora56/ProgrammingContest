class inst:
    def __init__(self, ty, dis):
        self.typ = ty
        self.distance = dis

a, b, q = map(int, input().split())
insts = [ inst("Shrine", int(input())) for _ in range(a)]
for _ in range(b):
    insts.append(inst("Temple", int(input())))
insts = sorted(insts, key = lambda x: x.distance)
question = [int(input()) for _ in range(q)]
for ins in insts:
    print(ins.typ + " in " + str(ins.distance))

def search(id, pos, mov, tpl, srn):
    small = float("inf")
    big = float("inf")
    for i in range(id + 1, len(insts)):
        if insts[i].typ == "Shrine":
            if not srn:
                big = abs(insts[i].distance - pos)
        elif insts[i].typ == "Temple":
            if not tpl:
                big = abs(insts[i].distance - pos)
    for i in range(id - 1, -1, -1):
        if insts[i].typ == "Shrine":
            if not srn:
                small = abs(insts[i].distance - pos)
        elif insts[i].typ == "Temple":
            if not tpl:
                small = abs(insts[i].distance - pos)
    return min([small, big]) + mov

for q in question:
    pos = q
    mov = 0
    if q <= insts[0].distance:
        tpl = False
        srn = False
        for i in insts:
            if i.typ == "Shrine":
                if not srn:
                    mov += i.distance - pos
                    pos = i.distance
                    srn = True
            elif i.typ == "Temple":
                if not tpl:
                    mov += i.distance - pos
                    pos = i.distance
                    tpl = True
            if srn and tpl:
                break
    elif q >= insts[len(insts) - 1].distance:
        tpl = False
        srn = False
        insts.reverse()
        for i in insts:
            if i.typ == "Shrine":
                if not srn:
                    mov += pos - i.distance
                    pos = i.distance
                    srn = True
            elif i.typ == "Temple":
                if not tpl:
                    mov += pos - i.distance
                    pos = i.distance
                    tpl = True
            if srn and tpl:
                insts.reverse()
                break
    else:
        start = -1
        for i in range(len(insts)):
            if insts[i].distance == q:
                move = search(i, q, 0, insts[i].typ == "Temple", insts[i].typ == "Shrine")
            elif insts[i].distance > q:
                a = search(i - 1, insts[i-1].distance, abs(insts[i-1].distance-q), insts[i-1].typ == "Temple", insts[i-1].typ == "Shrine")
                b = search(i + 1, insts[i+1].distance, abs(insts[i+1].distance-q), insts[i+1].typ == "Temple", insts[i+1].typ == "Shrine")
                move = min([a,b])
                break
    print(move)