import sys
input = sys.stdin.readline

n_home, cnt_modem = map(int,input().split())

coor = []
for _ in range(n_home):
    coor.append(int(input()))
coor.sort()

low, high = 0, coor[-1]
dis = 0

while low <= high:
    mid = (low+high)//2

    modem = [coor[0]]
    for i in range(1,len(coor)):
        if mid <= coor[i] - modem[-1]:
            modem.append(coor[i])

    if cnt_modem <= len(modem):
        dis = mid
        low = mid + 1
    else:
        high = mid - 1

print(dis)