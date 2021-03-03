import sys

def find_h(trs,h,l,tgt,answers,is_answer):
    # print("------------------------------------------------")
    if h < l or is_answer:
        return

    mid = (h+l)//2
    # print("mid : ",mid)

    remains = 0
    if (answers[0][1] == -1 or answers[0][1] < mid) and (answers[1][1] == 0 or mid < answers[1][1] ):
        for tr in trs:
            if tr >= mid:
                remains += (tr - mid)
        # print("r: ",remains)

        if remains < tgt:
            if answers[1][1] == 0 or mid < answers[1][1]:
                answers[1][1] = mid
                # print("new limit:",answers[1])

            if answers[0][1] == -1:
                find_h(trs, answers[1][1], 0, tgt, answers, is_answer)
            else:
                find_h(trs, answers[1][1], answers[0][1], tgt, answers, is_answer)

        elif remains > tgt:
            if answers[0][0] == -1 or remains - tgt < answers[0][0]:
                answers[0][0] = (remains - tgt)
                answers[0][1] = mid
                # print("new answer:",answers[0])

            if answers[1][1] == 0:
                find_h(trs, h, answers[0][1], tgt, answers, is_answer)
            else:
                find_h(trs, answers[1][1], answers[0][1], tgt, answers, is_answer)

        else:
            if answers[0][0] == -1 or remains - tgt < answers[0][0]:
                answers[0][0] = (remains - tgt)
                answers[0][1] = mid
                # print("new answer:", answers[0])
            is_answer = True
            return



n, m = map(int, sys.stdin.readline().rstrip().split())
trees = [int(i) for i in sys.stdin.readline().rstrip().split()]
high, low = max(trees), 0

answers = [[-1,-1],[0,0]]
is_answer = False
find_h(trees,high,low,m,answers,is_answer)

print(answers[0][1])
