import sys

def dolmen(c):
    sum = (c**2)*(c-1)//2
    print(sum)

n = int(input())
for _ in range(n):
    in_a, in_b = map(int,sys.stdin.readline().split())
    dolmen(in_a + in_b)