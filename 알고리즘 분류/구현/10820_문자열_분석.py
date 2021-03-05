import sys

while True:
    try:
        s = input()
        small, capital, digit, space = 0,0,0,0

        for c in s:
            if c == ' ':
                space += 1
            # elif ord('0') <= ord(c) and ord(c) <= ord('9'):
            elif '0' <= c and c <= '9':
                digit += 1
            elif ord('A') <= ord(c) and ord(c) <= ord('Z'):
                capital += 1
            elif ord('a') <= ord(c) and ord(c) <= ord('z'):
                small += 1
            else:
                pass
        print(small,capital,digit,space)
    except:
        break