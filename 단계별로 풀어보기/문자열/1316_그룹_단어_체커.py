def main():
    n = int(input())

    cnt = n
    for _ in range(n):
        visit = [False for _ in range(ord('z')+1 - ord('a'))]
        word = input()
        visit[ord(word[0]) - ord('a')] = True
        for i in range(1,len(word)):
            if word[i-1] != word[i]:
                if visit[ord(word[i])-ord('a')] == False:
                    visit[ord(word[i]) - ord('a')] = True
                else:
                    cnt -= 1
                    break
    print(cnt)

if __name__ == '__main__':
    main()