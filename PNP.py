# 情報基礎学A初回で見たやつ
LIS = [55,61,82,83,91,96,105,118,131]
NUM = 443

a = 1 << len(LIS)
for i in range(a):
    total = 0
    bit = i
    for j in range(len(LIS)):
        if bit & -bit == 1:
            total += LIS[j]
        bit = bit >> 1
    if total == NUM:
        op = ""
        bit = i
        for j in range(len(LIS)):
            if bit & -bit == 1:
                op += " {}".format(LIS[j])
            bit = bit >> 1
        print(op)
