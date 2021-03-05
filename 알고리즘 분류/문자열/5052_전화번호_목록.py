import sys
from collections import defaultdict
from pprint import pprint

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    tels = defaultdict(int)
    for _ in range(n):
        tels[sys.stdin.readline().rstrip()] = 1
    # pprint(tels)

    tels_cpy = dict(tels)
    # pprint(tels_cpy)
    is_consis = True
    for k, v in tels_cpy.items():
        for i in range(1,len(k)):
            if tels[k[:i]] == 1:
                print("NO")
                is_consis = False
                break
        if not is_consis:
            break
    if is_consis:
        print("YES")