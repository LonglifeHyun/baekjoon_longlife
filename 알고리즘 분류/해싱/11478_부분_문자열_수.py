s = input()

part = set()

for i in range(1,len(s)+1):
    for j in range(len(s)):
        if j+i < len(s)+1:
            part.add(s[j:j+i])
# print(part)
print(len(part))