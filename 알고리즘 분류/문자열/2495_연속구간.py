for _ in range(3):
    s = input()
    c = s[0]
    max_cnt = 1
    cnt = 1
    for i in range(1, len(s)):
        if c == s[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
            c = s[i]
    print(max_cnt)
