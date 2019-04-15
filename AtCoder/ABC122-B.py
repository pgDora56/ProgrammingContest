S = input()
count = 0
longest = 0
for l in S:
    if l in ['A', 'C', 'G', 'T']:
        count += 1
    else:
        if count > longest:
            longest = count
        count = 0

print(longest)
