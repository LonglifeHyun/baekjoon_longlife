import sys
input = sys.stdin.readline

n = int(input())

dp = [[1, 0]]
for i in range(n):
    dp.append([dp[-1][1], dp[-1][0] + dp[-1][1]])

print(dp[-1][0], dp[-1][1])