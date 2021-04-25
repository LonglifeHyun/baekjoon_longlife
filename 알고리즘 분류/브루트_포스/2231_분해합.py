n = int(input())

i = 0
while i < n:
    str_i = str(i)
    if i + sum(map(int,str_i)) == n:
        break
    i += 1

if i == n:
    print(0)
else:
    print(i)
