import sys

input = sys.stdin.readline

def add_move(q,v,n,idx,tgt):
    n += 1
    i, j = idx[0], idx[1]

    if 0 <= i-1 and 0 <= j-2 and not v[i-1][j-2]:   # 좌,좌상
        q.append([n, (i-1, j-2)])
        v[i-1][j-2] = True
        if i-1 == tgt[0] and j-2 == tgt[1]:
            return True, n
    if 0 <= i-2 and 0 <= j-1 and not v[i-2][j-1]:   # 상,좌상
        q.append([n, (i-2, j-1)])
        v[i-2][j-1] = True
        if i-2 == tgt[0] and j-1 == tgt[1]:
            return True, n
    if 0 <= i-2 and j+1 <= len(v)-1 and not v[i-2][j+1]:   # 상,우상
        q.append([n, (i-2, j+1)])
        v[i-2][j+1] = True
        if i-2 == tgt[0] and j+1 == tgt[1]:
            return True, n
    if 0 <= i-1 and j+2 < len(v)-1 and not v[i-1][j+2]:   # 우,우상
        q.append([n, (i-1, j+2)])
        v[i-1][j+2] = True
        if i-1 == tgt[0] and j+2 == tgt[1]:
            return True, n
    if i+1 <= len(v)-1 and j+2 <= len(v)-1 and not v[i+1][j+2]:   # 우,우하
        q.append([n, (i+1, j+2)])
        v[i+1][j+2] = True
        if i+1 == tgt[0] and j+2 == tgt[1]:
            return True, n
    if i+2 <= len(v)-1 and j+1 <= len(v)-1 and not v[i+2][j+1]:   # 하,우하
        q.append([n, (i+2, j+1)])
        v[i+2][j+1] = True
        if i+2 == tgt[0] and j+1 == tgt[1]:
            return True, n
    if i+2 <= len(v)-1 and 0 <= j-1 and not v[i+2][j-1]:   # 하,좌하
        q.append([n, (i+2, j-1)])
        v[i+2][j-1] = True
        if i+2 == tgt[0] and j-1 == tgt[1]:
            return True, n
    if i+1 <= len(v)-1 and 0 <= j-2 and not v[i+1][j-2]:   # 좌,좌하
        q.append([n, (i+1, j-2)])
        v[i+1][j-2] = True
        if i+1 == tgt[0] and j-2 == tgt[1]:
            return True, n

    return False, n

t_cs = int(input())
for _ in range(t_cs):
    l_side = int(input())
    src = tuple(map(int, input().rstrip().split()))
    dst = tuple(map(int, input().rstrip().split()))
    n_move = 0

    if src != dst:
        visit = [[False for _ in range(l_side)] for _ in range(l_side)]

        move_q = [[n_move,src]]
        visit[src[0]][src[1]] = True
        while len(move_q) != 0:
            present = move_q.pop(0)     # [0] : n_move, [1] : 좌표
            find_answer, n_move = add_move(move_q, visit, present[0], present[1], dst)

            if find_answer:
                break

    print(n_move)