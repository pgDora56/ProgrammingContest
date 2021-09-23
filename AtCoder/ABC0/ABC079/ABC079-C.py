abcd = input()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

op = ["+", "-"]
for op1 in op:
    for op2 in op:
        for op3 in op:
            val = a
            if op1 == "+":
                val += b
            else:
                val -= b

            if op2 == "+":
                val += c
            else:
                val -= c

            if op3 == "+":
                val += d
            else:
                val -= d
            
            if val==7:
                print("{}{}{}{}{}{}{}=7".format(a,op1,b,op2,c,op3,d))
                exit(0)