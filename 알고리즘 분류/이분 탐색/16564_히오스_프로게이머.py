import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = []

for _ in range(n):
    levels.append(int(input()))

min_lvl = min(levels)

low, high = min_lvl, min_lvl+k
max_t = 0

while low <= high:
    mid = (low+high)//2

    cnt_need = 0
    for lvl in levels:
        if lvl < mid:
            cnt_need += (mid-lvl)

    if cnt_need <= k:
        max_t = mid
        low = mid + 1
    else:
        high = mid - 1

print(max_t)