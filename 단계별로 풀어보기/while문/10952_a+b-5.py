def main():
    a, b = -1, -1
    ans = []
    while not(a==0 and b==0):
        ins = [int(i) for i in input().split()]
        a, b = ins[0], ins[1]
        ans.append(a+b)
    del ans[-1]

    for answer in ans:
        print(answer)

if __name__ == '__main__':
    main()