import sys

n = int(input())

my_stack = []

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "top":
        if len(my_stack) == 0:
            print("-1")
        else:
            print(my_stack[-1])
    elif cmd == "empty":
        if len(my_stack)==0:
            print("1")
        else:
            print("0")
    elif cmd == "size":
        print(len(my_stack))
    elif cmd == "pop":
        if len(my_stack)==0:
            print("-1")
        else:
            print(my_stack.pop(-1))
    else:
        my_stack.append(cmd.split()[-1])
