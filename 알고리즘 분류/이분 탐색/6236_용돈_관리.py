n, m = map(int, input().split())
use_money = []
for _ in range(n):
    use_money.append(int(input()))

low, high = max(use_money), sum(use_money)

k = []

while low <= high:
    mid = (low + high)//2

    draw = [0]
    for money in use_money:
        draw[-1] += money
        if draw[-1] > mid:
            draw[-1] -= money
            draw.append(money)

    if len(draw) <= m:
        k.append(mid)
        high = mid - 1
    else:
        low = mid + 1

k.sort()
print(k[0])