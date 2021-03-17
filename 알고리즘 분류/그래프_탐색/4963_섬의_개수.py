import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
    w, h = map(int, input().rstrip().split())

    if w == 0 and h == 0:
        break

    chart = [input().rstrip().split() for _ in range(h)]
    visit = [[False for _ in range(w)] for _ in range(h)]
    my_stack = []
    cnt = 0

    for i in range(h):
        for j in range(w):
            if chart[i][j] == '1' and not visit[i][j]:
                cnt += 1
                my_stack.append((i,j))
                visit[i][j] = True

                while len(my_stack) != 0:
                    tgt = my_stack.pop(-1)

                    idx_i, idx_j = tgt[0], tgt[1]

                    if 0 < idx_i and \
                            chart[idx_i-1][idx_j] == '1' and not visit[idx_i-1][idx_j]:         # 상
                        my_stack.append((idx_i-1, idx_j))
                        visit[idx_i-1][idx_j] = True
                    if idx_j < w-1 and \
                            chart[idx_i][idx_j+1] == '1' and not visit[idx_i][idx_j+1]:     # 우
                        my_stack.append((idx_i, idx_j+1))
                        visit[idx_i][idx_j+1] = True
                    if idx_i < h-1 and \
                            chart[idx_i+1][idx_j] == '1' and not visit[idx_i+1][idx_j]:     # 하
                        my_stack.append((idx_i+1, idx_j))
                        visit[idx_i+1][idx_j] = True
                    if 0 < idx_j and \
                            chart[idx_i][idx_j-1] == '1' and not visit[idx_i][idx_j-1]:       # 좌
                        my_stack.append((idx_i, idx_j-1))
                        visit[idx_i][idx_j-1] = True

                    if 0 < idx_i and 0 < idx_j and \
                            chart[idx_i-1][idx_j-1] == '1' and not visit[idx_i-1][idx_j-1]:   # 좌상
                        my_stack.append((idx_i-1, idx_j-1))
                        visit[idx_i-1][idx_j-1] = True
                    if 0 < idx_i and idx_j < w-1 \
                            and chart[idx_i-1][idx_j+1] == '1' and not visit[idx_i-1][idx_j+1]: # 우상
                        my_stack.append((idx_i-1, idx_j+1))
                        visit[idx_i-1][idx_j+1] = True
                    if idx_i < h-1 and idx_j < w-1 \
                            and chart[idx_i+1][idx_j+1] == '1' and not visit[idx_i+1][idx_j+1]: # 우하
                        my_stack.append((idx_i+1, idx_j+1))
                        visit[idx_i+1][idx_j+1] = True
                    if idx_i < h-1 and 0 < idx_j \
                            and chart[idx_i+1][idx_j-1] == '1' and not visit[idx_i+1][idx_j-1]:   # 좌하
                        my_stack.append((idx_i+1, idx_j-1))
                        visit[idx_i+1][idx_j-1] = True
                # for _ in visit:
                #     print(_)
                # print("--------------")
    print(cnt)
