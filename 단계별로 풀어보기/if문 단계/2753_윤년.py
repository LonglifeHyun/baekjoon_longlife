def is_leap(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    return False

def main():
    year = int(input())

    if is_leap(year):
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()