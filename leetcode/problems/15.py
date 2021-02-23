nums = list(map(int, input().split()))
res = []
nums.sort()
for i in range(len(nums)-2):
    l, r = i+1, len(nums)-1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            res.append((nums[i], nums[l], nums[r]))
            l += 1
            r -= 1

print(list(set(res)))
