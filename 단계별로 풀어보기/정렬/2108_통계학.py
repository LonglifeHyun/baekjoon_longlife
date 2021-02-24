import sys
n = int(input())

values = []

sum_v, max_v, min_v = 0, -4444, 4444
for _ in range(n):
    v = int(sys.stdin.readline())
    values.append(v)
    sum_v += v
    if max_v < v:
        max_v = v
    if v < min_v:
        min_v = v

print(round(sum_v/n))               # 산술평균

values.sort()
print(values[n//2])                 # 중앙값

#                                   # 최빈값
from collections import Counter

cnt = Counter(values)
cnts = cnt.most_common()
if len(cnts) == 1:
    print(cnts[0][0])
elif cnts[0][1] == cnts[1][1]:
    print(cnts[1][0])
else:
    print(cnts[0][0])

print(max_v-min_v)                  #범위

"""
n = int(input())

values = []

for _ in range(n):
    values.append(int(input()))

values.sort()

print(round(sum(values)/n))         # 산술평균
print(values[n//2])                 # 중앙값

#                                   # 최빈값
from collections import Counter

cnt = Counter(values)
cnts = cnt.most_common()
if len(cnts) == 1:
    print(cnts[0][0])
elif cnts[0][1] == cnts[1][1]:
    print(cnts[1][0])
else:
    print(cnts[0][0])

print(max(values)-min(values))      #범위
"""