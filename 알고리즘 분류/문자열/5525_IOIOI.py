"""
1. 문자열 s에서 Pn(IOI,IOIOI, ...) 을 모조리 찾아서, group에 추가.

    Pn을 찾는 과정은 다음과 같다.
    1-1. s를 순차탐색하면서 I를 찾음. 그리고 이때의 인덱스가 짝수인지 홀수인지도 체크.

    1-2. 만일 1-1에서 인덱스가 짝수일 경우, 해당 인덱스+1부터 남은 s를 순차탐색.
        짝수 인덱스에는 I가, 홀수 인덱스에는 O가 들어있어야 함.
        만일 이에 어긋나면 Pn이 아니라고 간주하고 break.
        break가 아닌 경우엔 string에 추가해서 Pn을 생성.
        이때 주의해야할 점이, II로 끝났을 경우에는 인덱스를 증가시키면 안됨.
        바로 그 I부터 찾아야 하니까 start_here라는 태그로 체크.

    1-3. 만일 1-1에서 인덱스가 홀수일 경우, 해당 인덱스+1부터 남은 s를 순차탐색.
        홀수 인덱스에는 I가, 짝수 인덱스에는 O가 들어있어야 함.
        만일 이에 어긋나면 Pn이 아니라고 간주하고 break.
        break가 아닌 경우엔 string에 추가해서 Pn을 생성.
        이때 주의해야할 점이, II로 끝났을 경우에는 인덱스를 증가시키면 안됨.
        바로 그 I부터 찾아야 하니까 start_here라는 태그로 체크.

    1-4. 최종적으로 생성된 패턴이 len_tgt보다 큰 경우엔 group에 추가.

2. group을 순차탐색하면서 가능한 개수 카운트.
    p가 tgt보다 길이가 길면 두칸씩 오른쪽으로 이동할 때마다 하나씩 카운트 증가.
    -> cnt += 1 + (len_p-len_tgt) // 2
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

tgt = "IO"*n+"I"
len_tgt = len(tgt)

group = []
idx = 0
start_here = False
while idx+1 < len(s):
    if s[idx]=='I':
        tmp_str = "I"
        if idx%2==0:
            idx += 1
            while idx < len(s):
                if idx%2!=0 and s[idx] == 'O':
                    tmp_str += 'O'
                elif idx%2!=0 and s[idx] == 'I':
                    start_here = True
                    break
                elif idx%2==0 and s[idx] == 'I':
                    tmp_str += 'I'
                elif idx%2==0 and s[idx] == 'O':
                    break
                idx += 1
        else:
            idx += 1
            while idx < len(s):
                if idx % 2 == 0 and s[idx] == 'O':
                    tmp_str += 'O'
                elif idx % 2 == 0 and s[idx] == 'I':
                    start_here = True
                    break
                elif idx % 2 != 0 and s[idx] == 'I':
                    tmp_str += 'I'
                elif idx % 2 != 0 and s[idx] == 'O':
                    break
                idx += 1

        if len(tmp_str) >= len_tgt:
            group.append(tmp_str)

    if start_here:
        start_here = False
    else:
        idx += 1

# print(group)
cnt = 0
for p in group:
    cnt += 1 + (len(p) - len_tgt)//2
print(cnt)