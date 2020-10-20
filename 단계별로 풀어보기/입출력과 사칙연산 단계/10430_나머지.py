def main():
    in_data = [int(i) for i in input().split()]
    a, b, c = in_data[0],in_data[1],in_data[2]
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)

if __name__ == '__main__':
    main()
