def main():
    ans = []
    while True:
        try:
            a, b = map(int, input().split())
            ans.append(a+b)
        except:
            break
    for answer in ans:
        print(answer)

    """
    try:
        while 1:
            n,k=map(int,input().split())
    except:exit()
    
    import sys
    for line in sys.stdin:
        n,k=map(int,line.split())
    """

if __name__ == '__main__':
    main()