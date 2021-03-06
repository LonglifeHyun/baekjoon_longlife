import sys
input = sys.stdin.readline

n = int(input())
present = {}
for _ in range(n):
    name, attend = input().rstrip().split()
    if present.get(name) == None:
        present[name] = 'Y'
    else:
        del present[name]

people = list(present.keys())
people.sort(reverse=True)
for name in people:
    print(name)
