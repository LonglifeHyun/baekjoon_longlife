import sys

input = sys.stdin.readline

n = int(input())

people = [list(map(int, input().rstrip().split())) for i in range(n)]

ranking = []
for i in range(n):      # 한 명 기준
    rank = 1
    for j in range(n):  # 모든 사람과 비교
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranking.append(rank)

for ranks in ranking:
    print(ranks, end=" ")

"""
# 잘못 짠거. 구현은 진짜 이게 맞나 싶은 정도로 그냥 짜면 됨. 
import sys

input = sys.stdin.readline

n = int(input())

people = [list(map(int, input().rstrip().split())) for i in range(n)]
for i in range(n):
    people[i].append(i)

people.sort(key=lambda x: (-x[0], -x[1]))

rankings = []
rank = 1
same_rank = 1
for i in range(len(people)-1):
    if people[i][0] > people[i+1][0] and people[i][1] > people[i+1][1]:
        rankings.append([rank,people[i][2]])
        rank += same_rank
    else:
        rankings.append([rank,people[i][2]])
        same_rank += 1
rankings.append([rank,people[n-1][2]])

rankings.sort(key=lambda x: x[1])
for ranks in rankings:
    print(ranks[0], end=' ')
    
# A: (5, 40), B: (3, 30), C: (2, 60) - 이런 경우 해결 못함.
"""