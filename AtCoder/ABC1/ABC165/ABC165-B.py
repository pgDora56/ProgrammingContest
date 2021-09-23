lim = int(input())
x = 100
y = 0
while x < lim:
    x += int(0.01*x)
    y += 1
print(y)
