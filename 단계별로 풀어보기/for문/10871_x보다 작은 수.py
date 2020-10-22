# https://www.acmicpc.net/problem/10871
import sys

def main():
    n, x = map(int, sys.stdin.readline().rstrip().split())
    num_list = [i for i in sys.stdin.readline().rstrip().split() if int(i) < x]

    for num in num_list:
        print(num,end=' ')

if __name__ == '__main__':
    main()