import sys
from collections import deque
input = sys.stdin.readline          # 이거 안하면 시간 초과

n = int(input())

sticks = deque()
for _ in range(n):
    sticks.append(int(input()))

max_high = sticks.pop()
cnt = 1
for _ in range(n-1):
    now = sticks.pop()
    if max_high < now:
        cnt += 1
        max_high = now
print(cnt)
