s = input()

alphabets = [0 for _ in range(ord('a'),ord('z')+1)]

for c in s:
    alphabets[ord(c)-ord('a')] += 1

for _ in alphabets:
    print(_,end=" ")