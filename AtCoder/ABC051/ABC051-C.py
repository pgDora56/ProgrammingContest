sx, sy, tx, ty = map(int, input().split())
x = tx - sx
y = ty - sy
op = ""
for i in range(y):
    op += "U"
for i in range(x):
    op += "R"
for i in range(y):
    op += "D"
for i in range(x):
    op += "L"
op += "L"
for i in range(y + 1):
    op += "U"
for i in range(x + 1):
    op += "R"
op += "DR"
for i in range(y + 1):
    op += "D"
for i in range(x + 1):
    op += "L"
op += "U"
print(op)
