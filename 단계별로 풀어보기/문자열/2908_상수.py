def main():
    num_a, num_b = map(str,input().split())
    num_a = num_a[::-1]
    num_b = num_b[::-1]

    print(max(num_a,num_b))

if __name__ == '__main__':
    main()