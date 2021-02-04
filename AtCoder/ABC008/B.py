n = int(input())
votes = {}
for _ in range(n):
    s = input()
    if s in votes:
        votes[s] += 1
    else:
        votes[s] = 1
votesl = list(votes.items())
votesl.sort(reverse=True, key=lambda x: x[1])

print(votesl[0][0])

