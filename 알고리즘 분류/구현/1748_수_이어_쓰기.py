n = input()

cnt = 0
for i in range(1,len(n)):
    cnt += i*(10**i - 10**(i-1))
cnt += len(n)*(int(n)-10**(len(n)-1)+1)
print(cnt)