def solve(nums, indexDifference, valueDifference):
    n = len(nums)
    min_index = 0
    max_index = 0
    for i in range(indexDifference, n):
        j = i - indexDifference
        if nums[j] < nums[min_index]:
            min_index = j
        if nums[j] > nums[max_index]:
            max_index = j

        if abs(nums[i] - nums[min_index]) >= valueDifference:
            return [i, min_index]

        if abs(nums[i] - nums[max_index]) >= valueDifference:
            return [i, max_index]
    return [-1, -1]