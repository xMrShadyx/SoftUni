nums_str = input().split(", ")
count = int(input())
nums = []



for num in nums_str:
    nums.append(int(num))

result_sum = [0] * count

for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]

print(result_sum)