n = int(input())
x = list(map(int, input().split()))

mini = float("inf")
for i in range(1, 101):
    total = 0
    for xs in x:
        total += pow(xs-i, 2)
    if total < mini:
        mini = total
print(mini)
