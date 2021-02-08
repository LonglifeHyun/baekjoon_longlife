import sys

n, m = map(int,sys.stdin.readline().split())
monsters = {}
answer = []
for i in range(n):
    monsters[i] = (sys.stdin.readline().rstrip())

reversed_mon = dict(map(reversed, monsters.items()))

for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        answer.append(monsters[int(tmp)-1])
    else:
        answer.append(reversed_mon[tmp]+1)

for _ in answer:
    print(_)
