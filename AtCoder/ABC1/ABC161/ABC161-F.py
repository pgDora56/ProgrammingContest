import math
n = int(input())

def makeprime(num):
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]

def search_divisor(num):
    num_sqrt = math.floor(math.sqrt(num))
    prime_list = makeprime(num_sqrt)

    divisor_num = 1
    cntone = 0
    for prime in prime_list:
        count = 1
        while num % prime == 0:
            num //= prime
            count += 1
        if count != 1: cntone += 1
        divisor_num *= count

    if num != 1:
        divisor_num *= 2

    return divisor_num


s = search_divisor(n-1) # ほんとは1を除くので-1、ただ自身を結局足すので
# d = 1 if n % 2 == 0 else 0
print(s + 1)

