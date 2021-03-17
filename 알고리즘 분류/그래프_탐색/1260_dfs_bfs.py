import sys
from collections import deque
input = sys.stdin.readline

def dfs(arr,num,src):
    answer = []
    visit = [False for _ in range(num+1)]
    stack = deque([src])

    while stack:
        node = stack.pop()
        if not visit[node]:
            answer.append(node)
            visit[node] = True
            stack.extend(reversed(arr[node]))

    return answer

def bfs(arr,num,src):
    answer = []
    visit = [False for _ in range(num+1)]
    queue = deque([src])
    visit[src] = True

    while queue:
        node = queue.popleft()
        answer.append(node)

        for v in arr[node]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
    return answer


num_v, num_e, src_v = map(int, input().rstrip().split())

vertex = [[] for _ in range(num_v+1)]
for _ in range(num_e):
    fst, snd = map(int, input().rstrip().split())
    vertex[fst].append(snd)
    vertex[snd].append(fst)

for vtx in vertex:
    vtx.sort()

dfs_ans = dfs(vertex, num_v, src_v)
bfs_ans = bfs(vertex, num_v, src_v)

for node in dfs_ans:
    print(node, end=' ')
print()
for node in bfs_ans:
    print(node, end=' ')
