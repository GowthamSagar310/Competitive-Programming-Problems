def smallestAbsent(nums) -> int:
    avg = sum(nums) // len(nums)
    s = set(nums)
    while True:
        if max(avg+1, 1) not in s:
            return max(avg+1, 1)
        avg += 1

nums = [-100]
print(smallestAbsent(nums))