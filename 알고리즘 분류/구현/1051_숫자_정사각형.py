"""
# re 라이브러리 아주 좋아!
import re

a = "asdfsdadsfaasdeee"

lst = []
for idx in re.finditer('a',a):
    lst.append(idx.start())
print(lst)
"""

import sys, re
from collections import Counter
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
rect = [input().rstrip() for _ in range(n)]

max_side = 0
idxs = []
for row in rect:
    cnter = Counter(row)

    temp = []
    for k, v in cnter.items():
        if v >= 2:
            tmp = []
            for idx in re.finditer(k, row):
                tmp.append(idx.start())
            temp.append([k,tmp])
    idxs.append(temp)

for i in range(len(idxs)):
    side = 0
    for j in range(len(idxs[i])):
        for pair in combinations(idxs[i][j][1],2):
            side = pair[1] - pair[0]
            if max_side != 0 and side <= max_side:
                continue
            elif i+side <= len(idxs)-1:
                for l in range(len(idxs[i+side])):
                    if idxs[i][j][0] == idxs[i+side][l][0]:
                        idx_set = set(idxs[i+side][l][1])
                        if pair[0] in idx_set and pair[1] in idx_set:
                            max_side = side
    if len(idxs) - i <= max_side:
        break

print((max_side+1)*(max_side+1))