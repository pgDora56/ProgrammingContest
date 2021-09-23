from fractions import Fraction
n = int(input())
def calc(x, y):
    return x[0] * y[0] + x[1] * y[1]

bothzero = 0
azero = 0
bzero = 0
iwashi = []
for _ in range(n):
    a,b = map(int,input().split())
    if a == 0:
        if b == 0:
            bothzero += 1
        else:
            azero += 1
    elif b == 0:
        bzero += 1
    else:
        iwashi.append(Fraction(a,b))

iwashi.sort(key=lambda i:i.numerator*i.denominator)
print(iwashi)

iwashidic = {}
now = ""
cnt = 0
for i in range(len(iwashi)):
    pass


