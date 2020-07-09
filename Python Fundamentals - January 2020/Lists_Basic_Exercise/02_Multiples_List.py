n1 = int(input())
n2 = int(input())

nums = []
for num in range(n1, n1 * n2 + 1, n1):
    nums.append(num)

print(nums)
