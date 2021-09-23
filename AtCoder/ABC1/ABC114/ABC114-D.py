def divisors_count(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return len(divisors)

n = int(input())
va = 1
for i in range(1, n + 1):
    va *= i

count = 0
rt = 1
v = 1
while v <= va:
    if va % v == 0:
        count += 1
    rt += 1
    v = rt  * rt
print(count)