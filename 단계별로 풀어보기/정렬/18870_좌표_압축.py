import sys
from collections import Counter

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))

cntr = Counter(nums)

zip = {}
for i, val in enumerate(sorted(list(cntr.keys()))):
    zip[val] = i

for num in nums:
    print(zip[num], end=' ')

"""
# sorted의 인자로 set이 들어가도 됨. 리스트 return 함. 

a = [1, 4, 7, 2, 44, 1, 76, 2]
print(set(a))
print(sorted(set(a)))
"""
