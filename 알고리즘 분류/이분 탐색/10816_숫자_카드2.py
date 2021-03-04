import sys, bisect

input = sys.stdin.readline

def cal_cnt(arr,x):
    idx_l = bisect.bisect_left(arr, x)
    idx_r = bisect.bisect_right(arr, x)
    # print("idx_l :",idx_l)
    # print("idx_r :",idx_r)

    if idx_l < len(arr) and idx_r < len(arr) and arr[idx_l] == x and arr[idx_r] == x:
        return idx_r - idx_l + 1    # idx_l, idx_r 둘 다 x의 인덱스인 경우.
    elif idx_l < len(arr) and idx_r == len(arr) and arr[idx_l] == x:
        return idx_r - idx_l        # idx_l만 x의 인덱스인 경우. idx_r이 인덱싱 범위 벗어났을 때.
    elif idx_l < len(arr) and arr[idx_l] == x and idx_l != idx_r:
        return idx_r - idx_l        # idx_l만 x의 인덱스인 경우. idx_r이 인덱싱 범위 내에 있을 때.
    else:
        return 0                    # x가 arr에 없는 경우.

n = int(input())
s_cards = list(map(int, input().split()))
m = int(input())
d_cards = list(map(int, input().split()))

s_cards.sort()
# print(s_cards)

for card in d_cards:
    print(cal_cnt(s_cards,card),end=' ')
