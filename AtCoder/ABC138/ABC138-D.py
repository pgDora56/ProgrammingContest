n, q = map(int,input().split())
nodes = [[[], 0] for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a-1][0].append(b-1)
for _ in range(q):
    p, q = map(int, input().split())
    nodes[p-1][1] += q

search_node = [0]

while len(search_node) > 0:
    n = search_node.pop()
    for i in nodes[n][0]:
        nodes[i][1] += nodes[n][1]
        search_node.append(i)


op = str(nodes[0][1])
for n in range(1, len(nodes)):
    op += " {}".format(nodes[n][1])
print(op)
