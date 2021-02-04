k = int(input())
val = [0]
for _ in range(k):
    if len(val) == 1:
        if val[0] != 9:
            val[0] += 1
        else:
            val.insert(0, 1)
            val[-1] = 0
    else:
        accept = False
        for i in range(1, len(val)):
            if val[-1*(i+1)] >= val[-1*i] and val[-1*i] != 9:
                val[-1*i] += 1
                for r in range(1,i):
                    val[-1*(i-r)] = max(0, val[-1*(i-r+1)]-1)
                accept = True
                break
        if not accept:
            if val[0] != 9:
                val[0] += 1
                for i in range(1, len(val)):
                    val[i] = max(val[i-1] - 1, 0)
            else:
                val.insert(0,1)
                for i in range(1, len(val)):
                    val[i] = 0

op = ""
for v in val:
    op += str(v)
print(op)

