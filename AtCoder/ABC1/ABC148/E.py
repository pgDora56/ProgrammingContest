n = int(input())
if n % 2 == 1:
    print(0)
    exit()

n = n // 10
score = n
while n > 4:
    n //= 5
    score += n
print(score)
