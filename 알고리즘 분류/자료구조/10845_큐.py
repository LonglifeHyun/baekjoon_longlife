import sys

input = sys.stdin.readline

n = int(input())
my_queue = []
for _ in range(n):
    cmd = input().rstrip()
    if cmd == "front":
        if len(my_queue) == 0:
            print("-1")
        else:
            print(my_queue[0])
    elif cmd == "back":
        if len(my_queue) == 0:
            print("-1")
        else:
            print(my_queue[-1])
    elif cmd == "empty":
        if len(my_queue) == 0:
            print("1")
        else:
            print("0")
    elif cmd == "size":
        print(len(my_queue))
    elif cmd == "pop":
        if len(my_queue) == 0:
            print("-1")
        else:
            print(my_queue.pop(0))
    else:
        my_queue.append(cmd.split()[-1])