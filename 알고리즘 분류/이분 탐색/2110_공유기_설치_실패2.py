import sys, itertools
input = sys.stdin.readline

n, c = map(int,input().split())

coor = []
for _ in range(n):
    coor.append(int(input()))
coor.sort()
# print("coor:", coor)

max_min_gap = 0

fst = coor.pop(0)
last = coor.pop(-1)
# print("coor:", coor)
for pair in itertools.combinations(coor,c-2):
    modem = [fst]
    modem += list(pair)
    modem.append(last)
    # print("modems : ",modem)
    min_gap = 999999
    for i in range(len(modem)-1):
        gap = modem[i+1]-modem[i]
        if gap < min_gap:
            min_gap = gap
    if max_min_gap < min_gap:
        max_min_gap = min_gap

print(max_min_gap)

