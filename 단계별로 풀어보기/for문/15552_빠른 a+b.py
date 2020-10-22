# https://www.acmicpc.net/problem/15552
import sys

def main():
    t = int(input())

    for i in range(t):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)

if __name__ == '__main__':
    main()