import sys

input = sys.stdin.readline

n_ask = int(input())

sum_ask = 0
max_ask = 0
asks = []
for i in input().split():
    ask = int(i)
    sum_ask += ask
    asks.append(ask)
    if max_ask < ask:
        max_ask = ask

budget = int(input())

low, high = 0, max_ask
cal_with_bound, max_budget = 0, 0

if sum_ask <= budget:
    print(max_ask)
else:
    while low <= high:
        mid = (low+high)//2

        cal_with_bound = 0
        for ask in asks:
            if ask <= mid:
                cal_with_bound += ask
            else:
                cal_with_bound += mid

        if cal_with_bound <= budget:
            max_budget = mid
            low = mid + 1
        else:
            high = mid - 1

    print(max_budget)
