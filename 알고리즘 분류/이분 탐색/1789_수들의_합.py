import sys
input = sys.stdin.readline

def sum2n(l,p_s,num):
    s = p_s
    s += sum(range(l+1,num+1))
    return s

n_sum = int(input())
low, high = 0, 1
pre_sum = 0

while True:
    # print("------------------------------------")
    cur_sum = sum2n(low, pre_sum, high)
    # print("pre_sum: ",pre_sum)
    if cur_sum >= n_sum:
        break
    pre_sum = cur_sum
    low = high
    high *= 2
# print("l, h : ", low, high)
# print("pre_sum:",pre_sum)

pre_low = low
s = 0
while low <= high:
    # print("------------------------------------")
    mid = (low + high) // 2

    s = sum2n(pre_low,pre_sum,mid)
    # print("l, h, m : ", low, high, mid)
    # print("pre_low, pre_sum:",pre_low,pre_sum)
    # print("s : ",s)
    if s <= n_sum:
        pre_sum = s
        pre_low = mid
        low = mid + 1
    else:
        high = mid - 1

if s > n_sum:
    print(mid-1)
else:
    print(mid)