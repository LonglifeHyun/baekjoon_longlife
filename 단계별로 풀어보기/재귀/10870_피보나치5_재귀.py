import sys
sys.setrecursionlimit(10**8)

n = int(input())


def fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num-1) + fib(num-2)


print(fib(n))