w = input()
evens = []
for x in w:
    if x in evens:
        evens.remove(x)
    else:
        evens.append(x)
if len(evens) == 0:
    print("Yes")
else:
    print("No")
