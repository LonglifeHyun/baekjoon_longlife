# 좀 더럽게 짠거같음..

def main():
    origin = input()
    num_split = list(origin)
    num_split.reverse()

    if len(num_split) < 2:
        num_split.append('0')
    origin = "".join(reversed(num_split))
    sum = int(num_split[0]) + int(num_split[1])
    num_split2 = list(str(sum))
    num_split2.reverse()
    new_num = num_split[0]+num_split2[0]
    cycle = 1

    while new_num != origin:
        nums = list(new_num)
        if len(nums) < 2:
            nums.append('0')
        nums.reverse()
        sum = int(nums[0]) + int(nums[1])

        num_split2 = list(str(sum))
        num_split2.reverse()
        new_num = nums[0] + num_split2[0]

        cycle += 1

    print(cycle)


if __name__ == '__main__':
    main()