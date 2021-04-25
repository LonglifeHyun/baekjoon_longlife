import sys
from collections import Counter
input = sys.stdin.readline

n = input().rstrip()
cntr = Counter(input().rstrip().split())
v = input().rstrip()

print(cntr[v])


"""
근데 걍 count 함수 쓰면 됨. 
import sys
input = sys.stdin.readline

N = input().rstrip()
nums = list(input().rstrip().split())
tgt = input().rstrip()
print(nums.count(tgt))
"""