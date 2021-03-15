import sys
input = sys.stdin.readline

n = int(input())
pairs = [[] for _ in range(n)]
for i in range(n):
    for j, path in enumerate(input().rstrip().split()):
        if path == '1':
            pairs[i].append(j)

answer = []

for i in range(n):
    visits = [0 for _ in range(n)]
    nodes = [i]

    while len(nodes) != 0:
        tgt = nodes.pop(0)

        for node in pairs[tgt]:
            if visits[node] == 0:
                nodes.append(node)
                visits[node] = 1
    answer.append(visits)

for _ in answer:
    for is_path in _:
        print(is_path, end=' ')
    print()