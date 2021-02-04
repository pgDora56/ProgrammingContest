x,y,z = map(int, input().split())
for i in range(z):
    if x < y:
        x += 1
    else:
        y += 1
print(min([x,y]))
