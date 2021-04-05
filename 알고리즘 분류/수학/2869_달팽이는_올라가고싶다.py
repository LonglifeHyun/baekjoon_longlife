import sys
a, b, v = map(int, sys.stdin.readline().rstrip().split())

day = (v-a)//(a-b)
if (v-a)%(a-b) == 0:
    print(day+1)
else:
    print(day+2)