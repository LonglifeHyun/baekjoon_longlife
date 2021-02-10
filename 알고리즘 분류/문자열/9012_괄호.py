import sys

def is_vps(ps):
    left_stack = 0

    if ps[0] == ')':
        return False
    left_stack += 1
    for i in range(1,len(ps)):
        if ps[i] == '(':
            left_stack += 1
        else:
            if left_stack > 0:
                left_stack -= 1
            else:
                return False
    if left_stack == 0:
        return True
    return False

t = int(input())
answer = []

for _ in range(t):
    ps = sys.stdin.readline().rstrip()
    if is_vps(ps):
        answer.append("YES")
    else:
        answer.append("NO")

for _ in answer:
    print(_)