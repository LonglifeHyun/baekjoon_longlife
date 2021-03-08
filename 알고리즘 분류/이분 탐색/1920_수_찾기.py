import sys, bisect
input = sys.stdin.readline

n = int(input())
ns = [int(i) for i in input().split()]
m = int(input())
ms = [int(i) for i in input().split()]

ns.sort()

for jungsoo in ms:
    idx = bisect.bisect_left(ns,jungsoo)
    if idx < len(ns) and ns[idx] == jungsoo:
        print(1)
    else:
        print(0)