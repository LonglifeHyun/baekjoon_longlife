n = int(input())


def make_pattern(is_blank, mid, i_idx, j_idx):
    if mid == 0:
        return

    for i in range(i_idx+mid, i_idx+2*mid):
        for j in range(j_idx+mid, j_idx+2*mid):
            is_blank[i][j] = True

    nxt = mid // 3
    make_pattern(is_blank, nxt, i_idx, j_idx)
    make_pattern(is_blank, nxt, i_idx, j_idx+mid)
    make_pattern(is_blank, nxt, i_idx, j_idx+2*mid)
    make_pattern(is_blank, nxt, i_idx+mid, j_idx)
    make_pattern(is_blank, nxt, i_idx+mid, j_idx+2*mid)
    make_pattern(is_blank, nxt, i_idx+2*mid, j_idx)
    make_pattern(is_blank, nxt, i_idx+2*mid, j_idx+mid)
    make_pattern(is_blank, nxt, i_idx+2*mid, j_idx+2*mid)
    return


def draw_stars(is_blank):
    for i in range(len(is_blank)):
        for j in range(len(is_blank)):
            if is_blank[i][j]:
                print(' ', end='')
            else:
                print('*', end='')
        print()


is_blank = [[False for _ in range(n)] for _ in range(n)]
make_pattern(is_blank, n//3, 0, 0)
draw_stars(is_blank)

