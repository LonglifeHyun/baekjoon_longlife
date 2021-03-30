import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
sz_chess = 8

board = [input().rstrip() for _ in range(n)]

min_cnt = 2500
for i in range(0, (n-sz_chess)+1):
    for j in range(0, (m-sz_chess)+1):
        cnt_b = 0
        cnt_w = 0
        for ii in range(i, i+sz_chess):
            for jj in range(j, j+sz_chess):
                if (ii+jj)%2==0 and board[ii][jj] == 'W':
                    # 'B'으로 시작했을 때, 'B'여야 하는 자리에 'W'일 경우. 수정해야할 칸으로 간주
                    cnt_b += 1
                elif (ii+jj)%2!=0 and board[ii][jj] == 'B':
                    # 'B'으로 시작했을 때, 'W'여야 하는 자리에 'B'일 경우. 수정해야할 칸으로 간주
                    cnt_b += 1
                elif (ii+jj)%2==0 and board[ii][jj] == 'B':
                    # 'W'으로 시작했을 때, 'W'여야 하는 자리에 'B'일 경우. 수정해야할 칸으로 간주
                    cnt_w += 1
                elif (ii+jj)%2!=0 and board[ii][jj] == 'W':
                    # 'W'으로 시작했을 때, 'B'여야 하는 자리에 'W'일 경우. 수정해야할 칸으로 간주
                    cnt_w += 1
        min_cnt = min(min_cnt,cnt_b,cnt_w)
print(min_cnt)
