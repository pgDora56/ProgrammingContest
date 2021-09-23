n, a, b = map(int, input().split())
s = input()

ap = 0
bp = 0

for c in s:
    if ap + bp >= a + b:
        print("No")
        continue

    if c == "a":
        print("Yes")
        ap += 1
        continue
    if c == "b":
        if bp < b:
            print("Yes")
            bp += 1
            continue
    print("No")
