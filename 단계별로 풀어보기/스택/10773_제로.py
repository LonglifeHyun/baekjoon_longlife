k = int(input())

num_stack = []
sum_money = 0
for i in range(k):
    tmp = int(input())
    if tmp == 0:
        sum_money -= num_stack.pop(-1)
    else:
        sum_money += tmp
        num_stack.append(tmp)

print(sum_money)
