import sys
input = sys.stdin.readline

def sum2n(num):
    return (num*(num+1))//2

n_sum = int(input())
"""
low, high = 1, 2

while True:
    cur_sum = sum2n(high)
    if cur_sum >= n_sum:
        break
    low = high
    high *= 2
"""
low, high = 1, n_sum
ans, s = 0, 0
while low <= high:
    mid = (low + high) // 2

    s = sum2n(mid)

    if s <= n_sum:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)