k, n = map(int, input().split())
youngs = []
for _ in range(k):
    youngs.append(int(input()))

low, mid, high = 0, 0, max(youngs)
answer = []

while low <= high:
    # print("------------------------------")
    cnt = 0
    mid = (low + high) // 2
    # print("mid: ",mid)
    if mid != 0 :
        for lan in youngs:
            cnt += lan//mid
    # print("cnt: ",cnt)
    if cnt >= n:
        answer.append(mid)
        # print("answer : ", answer)
        low, high = mid+1, high
    elif cnt < n:
        low, high = low, mid-1
    # print("low, high: ",low,high)

if len(answer) > 0:
    answer.sort(reverse=True)
    print(answer[0])
else:
    print("1")