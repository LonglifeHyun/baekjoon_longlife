def find_self_num(is_self_num,i):
    str_num = list(str(i))
    new_num = i
    for digit in str_num:
        new_num += int(digit)
    if new_num > 10000:
        return
    is_self_num[new_num] = False
    find_self_num(is_self_num,new_num)
    return

def main():
    is_self_num = [True for i in range(10001)]
    for i in range(1,10001):
        if is_self_num[i]:
            find_self_num(is_self_num,i)

    for i,self_num in enumerate(is_self_num):
        if i > 0:
            if self_num:
                print(i)

if __name__ == '__main__':
    main()