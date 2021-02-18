s = input()
cnt = 0

croatia = ["c=","c-","d-","lj","nj","s=","z="]      # "dz=" 는 따로 체크
croatia_c = ['c','d','l','n','s','z']

i=0
while i < len(s):
    if s[i] in croatia_c:
        if s[i]=='d':
            tmp = s[i:i+3]
            if tmp == "dz=":
                cnt += 1
                i += 3
            else:
                tmp = s[i:i + 2]
                if tmp in croatia:
                    cnt += 1
                    i += 2
                else:
                    cnt += 1
                    i += 1
        else:
            tmp = s[i:i+2]
            if tmp in croatia:
                cnt += 1
                i += 2
            else:
                cnt += 1
                i += 1
    else:
        cnt += 1
        i += 1

print(cnt)

