# sol 1
import sys

n = int(input())

registers = []

for _ in range(n):
    registers.append(tuple(sys.stdin.readline().rstrip().split()))

# ordered_registers = list(registers)       # shallow / deep copy 주의
# ordered_registers.sort(key=lambda x: (int(x[0]),registers.index((x[0],x[1]))))   # 시간 초과
registers.sort(key=lambda x: int(x[0]))     # 위처럼 할 필요가 없었음.

for p in registers:
    print(p[0],p[1])


"""
# sol 2

import sys

n = int(input())

registers = [[] for _ in range(200+1)]

for _ in range(n):
    tmp = tuple(sys.stdin.readline().rstrip().split())
    registers[int(tmp[0])].append(tmp)

for pp in registers:
    if len(pp) > 0:
        for p in pp:
            print(p[0],p[1])
"""