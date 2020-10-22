# https://www.acmicpc.net/problem/2741
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        print(i)                            # 104ms
        #sys.stdout.write(str(i) + '\n')    # 108ms
        #sys.stdout.writelines(str(i)+'\n') # 172ms

if __name__ == '__main__':
    main()