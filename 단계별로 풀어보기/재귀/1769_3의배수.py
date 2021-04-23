import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num = input().rstrip()      # 여기서 int로 받고 안에서 str처리하면 시간초과남.

def transfrom(n, ans):
    if len(n) < 2:
        if int(n)%3 != 0:
            ans[0] = "NO"
        return

    # nxt = 0
    # for i in n:
    #     nxt += int(i)

    nxt = sum(map(int,n)) # map을 이렇게도 쓸 수 있네. 시간 훨씬 빨라짐.

    ans[1] += 1
    transfrom(str(nxt), ans)

    return

answer = ["YES", 0]
transfrom(num, answer)
print(answer[1])
print(answer[0])

