def main():
    a = int(input())
    b = list(input())
    sum = 0
    for i,num in enumerate(reversed(b)):
        tmp = a*int(num)
        print(tmp)
        sum += tmp * 10**i
    print(sum)

if __name__ == '__main__':
    main()
