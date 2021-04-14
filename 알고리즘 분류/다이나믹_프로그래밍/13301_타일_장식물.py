n = int(input())

fib = {0: 0, 1: 1}
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]

print(fib[n]*2+(fib[n-1]+fib[n])*2)