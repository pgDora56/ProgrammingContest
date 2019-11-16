s = input()
stack = ""
for x in s:
    if x in ["0", "1"]:
        stack += x
    else:
        if len(stack) != 0:
            stack = stack[:-1]
print(stack)
