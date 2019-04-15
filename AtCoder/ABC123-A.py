sm = float('inf')
bi = - float('inf')
for _ in range(5):
    v = int(input())
    if v < sm: sm = v
    if v > bi: bi = v

if bi - sm > int(input()): print(':(')
else: print('Yay!')
