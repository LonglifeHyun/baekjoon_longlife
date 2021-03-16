import sys, bisect

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lessons = list(map(int, input().rstrip().split()))
# print("lessons : ", lessons)

answer = []

low, high = max(lessons), sum(lessons)
while low <= high:
    # print("--------------------------------")
    mid = (low+high)//2
    # print("low, high, mid :", low, high, mid)

    blue = [lessons[0]]
    for i in range(1, len(lessons)):
        blue[-1] += lessons[i]
        if blue[-1] > mid:
            blue[-1] -= lessons[i]
            blue.append(lessons[i])
    # print(blue)

    if len(blue) <= m:
        answer.append(mid)
        # print("answer : ", answer)
        high = mid - 1
    else:
        low = mid + 1

answer.sort()
print(answer[0])
