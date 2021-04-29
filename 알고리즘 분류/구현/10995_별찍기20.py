n = int(input())

for i in range(n):
    for _ in range(n):
        if i%2 == 0:
            print('* ',end='')
        else:
            print(' *',end='')
    print()