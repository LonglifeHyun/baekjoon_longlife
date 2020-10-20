def main():
    ins = [int(i) for i in input().split()]
    h, m = ins[0], ins[1]

    change_h = False
    if m < 45:
        change_h = True
        m = (m+60)-45
    else:
        m = m-45

    if change_h == True:
        if h == 0:
            h = 23
        else:
            h -= 1

    print(h,m)

if __name__ == '__main__':
    main()