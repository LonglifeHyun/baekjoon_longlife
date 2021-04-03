for c in input():
    if c.islower():
        print(c.upper(),end='')
    else:
        print(c.lower(),end='')

# print(input().swapcase()) : lower -> upper ,  upper -> lower