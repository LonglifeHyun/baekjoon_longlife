num = int(input())

def to_binary(n):
    if n == 0:
        return ""

    return str(n%2)+to_binary(n//2)


print(to_binary(num)[::-1])