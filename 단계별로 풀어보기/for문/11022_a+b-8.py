# https://www.acmicpc.net/problem/11022
import sys

def main():
    t = int(sys.stdin.readline())

    for i in range(1,t+1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print("Case #"+str(i)+":",a,"+",b,"=",a+b)

if __name__ == '__main__':
    main()