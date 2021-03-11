import sys, bisect

input = sys.stdin.readline

n = int(input())

property_vals = [int(i) for i in input().split()]
property_vals.sort()
# print("property_vals : ", property_vals)
idx = bisect.bisect_left(property_vals, 0)
neg_pro_vals = list(property_vals[:idx])
pos_pro_vals = list(property_vals[idx:])

mix_val = 0
answer = [2000000000,-1,-1]                # 혼합 특성값, 두 용액 특성값
for i in range(len(neg_pro_vals)):
    # print("=========================================================")

    low, high = 0, len(pos_pro_vals)-1

    while low <= high:
        # print("----------------------------------------------")
        mix_val = neg_pro_vals[i]
        # print("a : ", mix_val)

        mid = (low+high)//2

        # print("low, high, mid : ",low, high, mid)
        # print("b : ", pos_pro_vals[mid])
        mix_val += pos_pro_vals[mid]
        # print("mix_val : ",mix_val)
        if abs(mix_val) < abs(answer[0]):
            answer = mix_val, neg_pro_vals[i], pos_pro_vals[mid]
            # print("answer: ", answer)
        if mix_val == 0:
            # print("here1")
            break
        elif mix_val < 0:
            # print("here2")
            low = mid + 1
        else:
            # print("here3")
            high = mid - 1

    if answer[0] == 0:
        # print("here4")
        break

if len(neg_pro_vals) >= 2:
    mix_val = neg_pro_vals[-2] + neg_pro_vals[-1]
    if abs(mix_val) < abs(answer[0]):
        answer = mix_val, neg_pro_vals[-2], neg_pro_vals[-1]

if len(pos_pro_vals) >= 2:
    mix_val = pos_pro_vals[0] + pos_pro_vals[1]
    if abs(mix_val) < abs(answer[0]):
        answer = mix_val, pos_pro_vals[0], pos_pro_vals[1]

print(answer[1], answer[2])


