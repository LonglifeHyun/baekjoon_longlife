"""
ex : [][]([[]())] - NO
"""

import sys

def is_vps(s):
    ps = ['(',')','[',']']
    shape = ""
    left_stack1, left_stack2 = 0, 0  # 1: ()  2: []

    for c in s:
        if c in ps:
            if (left_stack1 == 0 and c == ')') or (left_stack2 == 0 and c == ']'):
                return False

            if c == '(':
                shape += '('
                left_stack1 += 1
            elif c == '[':
                shape += '['
                left_stack2 += 1
            elif c == ')':
                if shape[len(shape)-1] == '[':
                    return False
                shape = shape[:len(shape)-1]
                left_stack1 -= 1
            elif c == ']':
                if shape[len(shape)-1] == '(':
                    return False
                shape = shape[:len(shape)-1]
                left_stack2 -= 1

    if left_stack1 == 0 and left_stack2 == 0:
        return True
    return False

answer = []

s = sys.stdin.readline().rstrip()
while not s == ".":
    if is_vps(s):
        answer.append("yes")
    else:
        answer.append("no")

    s = sys.stdin.readline().rstrip()

for _ in answer:
    print(_)