import sys, re
input = sys.stdin.readline

s = input().rstrip()

j_cnt = len(re.findall("JOI", s))
print(j_cnt)

i_cnt = 0
for ioi in re.finditer("IO", s):
    if ioi.start()+2 < len(s) and s[ioi.start()+2] == 'I':
        i_cnt += 1
print(i_cnt)