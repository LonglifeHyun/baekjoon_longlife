import sys
input = sys.stdin.readline

num_v, num_e = map(int, input().rstrip().split())

pairs = [[] for _ in range(num_v+1)]
for _ in range(num_e):
    fst, snd = map(int, input().rstrip().split())
    pairs[fst].append(snd)
    pairs[snd].append(fst)

cnt = 0
vertexs = {i for i in range(1, num_v+1)}
# print("vertexs: ", vertexs)
visits = [False for i in range(num_v+1)]

while len(vertexs) != 0:
    cnt += 1
    nodes = [vertexs.pop()]
    visits[nodes[0]] = True

    while len(nodes) != 0:
        tgt = nodes.pop(0)
        vertexs.discard(tgt)

        for v in pairs[tgt]:
            if not visits[v]:
                nodes.append(v)
                visits[v] = True

print(cnt)