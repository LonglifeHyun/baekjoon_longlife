import sys

sums = 0

for i in sys.stdin.readline().rstrip().split():
    sums += int(i)**2

print(sums%10)