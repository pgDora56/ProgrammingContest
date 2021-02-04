s = input()
t = input()

let = len(t)
for i in range(len(s)-len(t)+1):
    tmp = len(t)
    for j in range(len(t)):
        if s[i+j] == t[j]:
            tmp -= 1
    let = min(let,tmp)
print(let)
