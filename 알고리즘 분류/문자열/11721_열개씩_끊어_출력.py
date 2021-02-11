import sys

word = sys.stdin.readline().rstrip()

i = 0
while len(word)-i > 10:
    print(word[i:i+10])
    i += 10
print(word[i:len(word)])