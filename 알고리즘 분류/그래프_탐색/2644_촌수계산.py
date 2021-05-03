import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
tgt_a, tgt_b = map(int, input().rstrip().split())
m = int(input().rstrip())

relations = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().rstrip().split())
    relations[parent].append(child)
    relations[child].append(parent)

visit = [False for _ in range(n+1)]
stk = deque()
for v in relations[tgt_a]:
    stk.append([v, 0])

is_relative = False
answer = 0

while len(stk) != 0:
    node = stk.pop()
    tgt, path = node[0], node[1]

    if tgt == tgt_b:
        is_relative = True
        answer = path+1
        break

    if not visit[tgt]:
        visit[tgt] = True

        for v in relations[tgt]:
            if not visit[v]:
                stk.append([v, path+1])

if is_relative:
    print(answer)
else:
    print(-1)