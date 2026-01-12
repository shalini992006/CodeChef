n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    nums = [a, b, c]
    nums.sort()
    print(nums[1])
