import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}
for _ in range(n):
    tmp = input().split()
    memo[tmp[0]] = tmp[1]

for _ in range(m):
    print(memo[input().rstrip()])