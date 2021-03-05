import sys, itertools
from collections import defaultdict
from pprint import pprint

input = sys.stdin.readline

k = int(input())
for _ in range(k):
    n = int(input())
    kinds = defaultdict(int)
    for _ in range(n):
        kinds[input().split()[1]] += 1
    # pprint(kinds)

    # num_kinds = list(kinds.values())
    # print(num_kinds)
    """
    [메모리 초과]
    for i in range(1,len(num_kinds)+1):
        combs = list(itertools.combinations(num_kinds,i))
        print(combs)

        sigma = 0
        for com in list(itertools.combinations(num_kinds,i)):
            print("----------------------------")
            tmp = 1
            for j in com:
                # print("j: ",j)
                tmp *= j
            print("tmp: ",tmp)
            sigma += tmp
            print("sigma: ",sigma)
        cnt += len(combs)*sigma
        cnt += sigma
        print("cnt: ",cnt)
        print()
    """
    cnt = 1
    for i in kinds.values():
        cnt *= (i+1)
    cnt -= 1

    print(cnt)