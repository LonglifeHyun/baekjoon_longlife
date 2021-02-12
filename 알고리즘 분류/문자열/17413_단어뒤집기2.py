import sys

s = sys.stdin.readline().rstrip()

turn = []
tags = []
tag, new_s = "", ""
i = 0
while i < len(s):
    if s[i] == '<':
        while i < len(s) and not(s[i] == '>'):
            tag += s[i]
            i += 1
        tag += s[i]
        turn.append('T')
        tags.append(tag)
        tag = ""
        i += 1
    else:
        while i < len(s) and not(s[i] == '<'):
            if s[i] == ' ':
                turn.append('R')
            new_s += s[i]
            i += 1
        turn.append('R')
        new_s += ' '

# print(tags)
# print(new_s)
reversed_s = [string[::-1] for string in new_s.split()]
# print(reversed_s)
# print(turn)

j, k = 0, 0
for ii in range(len(turn)):
    if turn[ii] == 'T':
        print(tags[j],end='')
        j += 1
    elif turn[ii] == 'R':
        if ii<len(turn)-1 and turn[ii+1]=='T':
            print(reversed_s[k], end='')
        else:
            print(reversed_s[k],end=' ')
        k += 1