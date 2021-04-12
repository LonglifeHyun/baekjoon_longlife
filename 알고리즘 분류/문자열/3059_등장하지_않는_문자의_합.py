t = int(input())
for _ in range(t):
    print(sum([ord(i) for i in list({chr(i) for i in range(ord('A'),ord('Z')+1)} - set(input()))]))
