import sys, itertools
input = sys.stdin.readline

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(input().rstrip('\n'))
integers = set()
for pair in itertools.permutations(cards,k):
    tmp = ""
    for i in pair:
        tmp += i
    integers.add(tmp)

print(len(integers))
