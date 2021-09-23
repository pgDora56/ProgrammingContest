import copy

a = []
b = copy.deepcopy(a)

a.append(1)
print(a)
print(b)

