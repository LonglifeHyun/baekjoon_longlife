# https://www.acmicpc.net/problem/2439

def main():
    n = int(input())

    for i in range(1,n+1):
        print(' '*(n-i)+'*'*i)

if __name__ == '__main__':
    main()