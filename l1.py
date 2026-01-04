from collections import defaultdict
def solve(nums, k):
    mini = float("inf")
    l = 0
    window = defaultdict(int)
    s = 0
    for r in range(len(nums)):
        window[nums[r]] += 1
        if window[nums[r]] == 1: s += nums[r]

        while l < r and nums[l] == nums[r]:
            window[nums[l]] -= 1
            l += 1
        
        while l <= r and s >= k:
            mini = min(mini, r-l+1)
            if window[nums[l]] == 1:
                s -= nums[l]
            window[nums[l]] -= 1
            l += 1
    return mini if mini != float("inf") else -1

nums = [18,18,19,19,21,22]
k = 39
print(solve(nums, k))