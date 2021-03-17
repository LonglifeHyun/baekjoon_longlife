import sys
from collections import deque

input = sys.stdin.readline

def is_valid(visit,z,y,x):
    if not (0 <= z <= len(visit)-1):
        return False
    if not (0 <= y <= len(visit[0])-1):
        return False
    if not (0 <= x <= len(visit[0][0])-1):
        return False
    if visit[z][y][x]:
        return False
    return True

def bfs_ripen(ripen_q,visit,non_ripe,dirs):
    max_day = 0
    is_break = False
    while len(ripen_q) != 0:
        day, pos = ripen_q.popleft()

        day += 1
        for dr in dirs:
            i, j, k = pos[0]+dr[0], pos[1]+dr[1], pos[2]+dr[2]
            if is_valid(visit,i,j,k):
                non_ripe -= 1
                ripen_q.append([day,(i,j,k)])
                visit[i][j][k] = True
                if max_day < day:
                    max_day = day
                if non_ripe == 0:
                    is_break = True
                    break
        if is_break:
            break
    return non_ripe, max_day


col, row, hei = map(int, input().rstrip().split())
visit = [[[False]*col for _ in range(row)] for _ in range(hei)]

ripen_q = deque()
days = 0
non_ripe = 0
for i in range(hei):
    for j in range(row):
        tomato = input().rstrip().split()
        for k in range(len(tomato)):
            if tomato[k] == '1':
                ripen_q.append([days,(i,j,k)])
                visit[i][j][k] = True
            elif tomato[k] == '-1':
                visit[i][j][k] = True
            elif tomato[k] == '0':
                non_ripe += 1

if non_ripe == 0 or len(ripen_q) == 0:
    print(days)
else:
    dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    non_ripe, days = bfs_ripen(ripen_q,visit,non_ripe,dirs)
    if non_ripe == 0:
        print(days)
    else:
        print(-1)