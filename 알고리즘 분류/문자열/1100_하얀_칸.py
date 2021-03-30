import sys
input = sys.stdin.readline

sz_chess = 8

cnt = 0
for i in range(sz_chess):
    s = input().rstrip()
    for j in range(sz_chess):
        if (i+j)%2 == 0 and s[j]=='F':
            cnt += 1
print(cnt)

"""
이런것도 됨. 여기서는 안써도 되는데 앞으로 써먹을 수도 있음. 

from collections import Counter

cntr = Counter('')
for _ in range(8):
    cntr += Counter(input().rstrip())
    print(cntr)
"""