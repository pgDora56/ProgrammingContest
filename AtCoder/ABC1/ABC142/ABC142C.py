stu = 0
def g(val):
    global stu
    stu += 1
    return [stu, int(val)]

n = int(input())
a = list(map(g, input().split()))
a.sort(key=lambda x: x[1])

op = str(a[0][0])
for i in range(1,n):
    op += " " + str(a[i][0])
print(op)

