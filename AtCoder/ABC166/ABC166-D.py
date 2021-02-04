x = int(input())

a = 1
b = 0

def val():
    global a, b
    if pow(a,5) - pow(-b,5) == x:
        b = -b
        return True
    return pow(a,5) - pow(b,5) == x

while not val():
    if a >= b:
        b += 1
    else:
        a += 1
        b = 0
print(a,b)
