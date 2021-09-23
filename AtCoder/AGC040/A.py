def calc(i):
    if i < 0:
        return 0
    if i <= 1:
        return i
    return (1+i) * i // 2


def colab():
    global m1, m2, total
    if m1 < m2:
        m1 -= 1
    else:
        m2 -= 1
    total += calc(m1) + calc(m2)
    m1 = 0
    m2 = 0


s = input()

m1 = 0
m2 = 0
total = 0

is_inc = True

for c in s:
    if c == "<":
        if not is_inc:
            colab()
        is_inc = True
        m1 += 1
    else:
        is_inc = False
        m2 += 1

colab()

print(total)
