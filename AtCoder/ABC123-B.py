import math
minutes = []
for _ in range(5):
    minutes.append(int(input()))
minutes.sort(reverse = True, key = lambda x: x % 10 if x % 10 != 0 else 10)
x = 0
for minute in minutes:
    x = math.ceil(x / 10) * 10
    x += minute
print(x)


