n = int(input())

for i in range(1,n+1):
    star = i+(i-1)
    sp = (n-1)-i+1
    print(' '*sp+'*'*star)