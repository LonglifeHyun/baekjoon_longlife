import sys

input = sys.stdin.readline

for s in input().rstrip().split('-'):
    print(s[0],end='')