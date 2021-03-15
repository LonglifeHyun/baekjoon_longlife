# n = int(input())
# k = int(input())

n = 5
for ii in range(1, 26):
    k = ii
    print("********************************************************************************")
    print("k: ",k)
    cnt_dict = {0: 0}
    cnt = 0
    for i in range(1, k//n+1):
        cnt += 1 + 2*(n-i)
        cnt_dict[i] = cnt
    # print("cnt_dict : ", cnt_dict)

    dis, idx_i, idx_j = 0, 0, 0
    stand_num = 0
    idx_i = k//n
    while idx_i >= 0:
        # print("=======================================================")

        i_cnt = cnt_dict[idx_i]
        # print("i_cnt : ", i_cnt)

        stand_num = idx_i * n
        # print("stand_num : ", stand_num)

        if idx_i == 0:
            idx_j = 0
            j_cnt = 0
        else:
            idx_j = (stand_num - 1) // (idx_i+1)
            max_add = idx_j - idx_i
            # print("max_add, idx_j, idx_i : ", max_add, idx_j, idx_i)
            j_cnt = (max_add * (max_add + 1)) // 2
            # print("j_cnt : ", j_cnt)

        cnt = i_cnt + j_cnt
        # print("cnt : ", cnt)

        if cnt <= k:
            # print("i_here1")
            dis = k - cnt
            break
        idx_i -= 1


    print("idx_i : ", idx_i)
    print("idx_j : ", idx_j)
    print("dis : ", dis)
    if dis == 0:
        if idx_i == 0:
            print(idx_j)
        else:
            print(idx_i*n)
    else:
        idx_i += 1
        idx_j += 1

        if idx_i >= n//2:
            cnt_lines = {}
            cnt_add = 0
            for ii in range(idx_j,n+1):
                cnt_add += ii - idx_i + 1
                cnt_lines[ii] = cnt_add

            low_j, high_j = idx_j, n

            j_line = 0
            dis2 = 0
            while low_j <= high_j:
                mid_j = (low_j + high_j) // 2

                if cnt_lines[mid_j] <= dis:
                    idx_j = mid_j
                    dis2 = dis - cnt_lines[mid_j]
                    low_j = mid_j + 1
                else:
                    high_j = mid_j - 1

            print("idx_i : ", idx_i)
            print("idx_j : ", idx_j)
            print("dis2 : ", dis2)

            if dis2 == 0:
                if (idx_j - idx_i + 1)%2==0:
                    idx_i = (idx_i + idx_j) // 2
                    idx_j = (idx_i + idx_j) // 2 + 1
                    print(idx_i*idx_j)
                else:
                    idx_i = (idx_i + idx_j) // 2
                    idx_j = (idx_i + idx_j) // 2
                    print(idx_i * idx_j)
            else:
                idx_j += 1
                dis2 -= 1
                gap = dis2 // 2
                idx_i = idx_i + gap
                idx_j = idx_j - gap
                print(idx_i*idx_j)
        else:
            cnt_lines = {}
            cnt_add = 0
            for k in range(idx_j, n + 1):
                cnt_add += k - idx_i + 1
                cnt_lines[k] = cnt_add

            low_j, high_j = idx_j, n

            j_line = 0
            dis2 = 0
            while low_j <= high_j:
                mid_j = (low_j + high_j) // 2

                if cnt_lines[mid_j] <= dis:
                    idx_j = mid_j
                    dis2 = dis - cnt_lines[mid_j]
                    low_j = mid_j + 1
                else:
                    high_j = mid_j - 1

            print("idx_i : ", idx_i)
            print("idx_j : ", idx_j)
            print("dis2 : ", dis2)
            print()
    print("######################################################################")