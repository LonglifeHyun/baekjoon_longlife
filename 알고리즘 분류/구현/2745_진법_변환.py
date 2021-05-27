n, b = input().split()

bb = int(b)
i = len(n)-1
res = 0
for c in n:
    if c.isalpha():
        pos = ord(c)-ord('A')+10
    else:
        pos = int(c)

    res += pos * (bb**i)
    i -= 1

print(res)