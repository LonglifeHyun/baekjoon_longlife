import sys
input = sys.stdin.readline

n = int(input())

cars_a = {}
for i in range(n):
    cars_a[input().rstrip()] = i

cars_b = []
for i in range(n):
    cars_b.append(input().rstrip())

cars_b.reverse()

cnt = 0

i = 0
while i < len(cars_b)-1:
    slow = cars_a[cars_b[i]]
    # print("slow : ",slow)
    j = i+1
    # print("fast : ",cars_a[cars_b[j]])
    while j < len(cars_b) and slow < cars_a[cars_b[j]]:
        cnt += 1
        j += 1
        # print("kkk")
    i = j

print(cnt)