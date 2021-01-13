def main():
	n = int(input())
	nums = []

	for i in range(n):
		nums.append(int(input()))
	# print(nums)

	nums.sort()
	# print(nums)

	for num in nums:
		print(num)


if __name__ == "__main__":
	main()