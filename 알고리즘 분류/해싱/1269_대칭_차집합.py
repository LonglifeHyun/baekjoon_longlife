import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}

print(len(a-b)+len(b-a))