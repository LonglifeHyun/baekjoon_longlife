import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def valid_check(s, pairs):
    stk = deque()

    i = 0
    while i < len(s):
        if len(stk) == 0 and (s[i] == ')' or s[i] == ']'):
            return False
        if s[i] == '(':
            stk.append([2, i])
        elif s[i] == '[':
            stk.append([3, i])
        elif s[i] == ')':
            if stk[-1][0] == 3:
                return False
            else:
                shape, idx = stk.pop()
                pairs.append([shape, idx, i])
        elif s[i] == ']':
            if stk[-1][0] == 2:
                return False
            else:
                shape, idx = stk.pop()
                pairs.append([shape, idx, i])
        i += 1

    if len(stk) != 0:
        return False
    return True


def cal_value(i, pairs, visit, limit):
    res = 0

    if pairs[i][2] - pairs[i][1] == 1:
        visit[i] = True
        res += pairs[i][0]

    while i < len(pairs) and pairs[i][1] < limit:
        if not visit[i] and (pairs[i][2]-pairs[i][1] > 1):
            if i+1 < len(pairs):
                res += pairs[i][0] * cal_value(i+1, pairs, visit, pairs[i][2])
                visit[i] = True

        if not visit[i] and (pairs[i][2] - pairs[i][1] == 1):
            visit[i] = True
            res += pairs[i][0]

        i += 1
    # print("res ", res)
    return res


paren = input().rstrip()
idx_pairs = []

if valid_check(paren, idx_pairs):
    idx_pairs.sort(key=lambda x: x[1])
    visit = [False for _ in range(len(idx_pairs))]
    print(cal_value(0, idx_pairs, visit, len(paren)))
else:
    print(0)