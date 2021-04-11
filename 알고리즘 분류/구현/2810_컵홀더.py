n = int(input())
s = input()
l_cnt = s.count('L')
if l_cnt == 0:
    print(n)
else:
    print(n+1 - l_cnt//2)