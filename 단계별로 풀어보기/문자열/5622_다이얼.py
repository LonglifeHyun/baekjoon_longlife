def main():
    word = input()

    time = len(word)
    for c in word:
        if c < 'S':
            dial = (ord(c) - ord('A')) // 3 + 2
        elif c < 'Z':
            dial = (ord(c) - ord('A') - 1) // 3 + 2
        else:
            dial = (ord(c) - ord('A') - 2) // 3 + 2
        time += dial
    print(time)

if __name__ == '__main__':
    main()

