import sys
input = sys.stdin.readline

tst_cs = int(input())
for _ in range(tst_cs):
    pos, s = input().rstrip().split()
    print(s[0:int(pos)-1]+s[int(pos):len(s)])