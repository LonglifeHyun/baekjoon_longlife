import sys
input = sys.stdin.readline

num_com = int(input())
num_pair = int(input())

pairs = [[] for _ in range(num_com+1)]
for _ in range(num_pair):
    fst, snd = map(int,input().rstrip().split())
    pairs[fst].append(snd)
    pairs[snd].append(fst)
# print("pairs:",pairs)

virus = {1}
check = pairs[1]

while len(check) != 0:
    for com in pairs[check[0]]:
        if com not in virus:
            check.append(com)
            # print(check)
    virus.add(check.pop(0))
    # print(virus)

print(len(virus)-1)
