import sys
input = sys.stdin.readline

t = int(input())
for tst_cs in range(t):
    n = int(input())
    # note1 = {int(i) for i in input().rstrip().split()}    # set일 때
    note1 = {int(i):1 for i in input().rstrip().split()}    # dict일 때
    m = int(input())
    note2 = [int(i) for i in input().rstrip().split()]

    for i in note2:
        # if i in note1:            # set일 때
        if note1.get(i) != None:    # dict일 때
            print(1)
        else:
            print(0)