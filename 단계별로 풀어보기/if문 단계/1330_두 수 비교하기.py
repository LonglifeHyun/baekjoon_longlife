def main():
    ins = [int(i) for i in input().split()]
    a, b = ins[0], ins[1]

    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")

if __name__ == '__main__':
    main()