Lower Bound find the first index where nums[i] >= target
Example: nums = [1, 2, 4, 4, 4, 6, 7] target = 4
LB: Index 2 (The first 4).
UB: Index 5 (The 6, because it's the first number strictly greater than 4).
Count of 4s: UB - LB = 5 - 2 = 3.



```python
left, right = 0, n-1
ans = n # if no value is found, we can insert it at the last index
while left <= right:
    mid = (left + right) >> 1
    if nums[mid] >= target:
        ans = mid 
        right = mid-1
    else:
        left = mid+1
return ans

# ans is initialized to n and there are chances we never find value >= target
# so we need to check before accessing 

```

Upper Bound find the first index where nums[i] > target

```python
left, right = 0, n-1
ans = n
while left <= right:
    mid = (left + right) >> 1
    if nums[mid] > target:
        ans = mid 
        right = mid-1
    else:
        left = mid+1
return ans
```

python library: bisect
bisect.bisect_left(arr, target) # lower_bound
bisect.bisect_right(arr, target) # upper_bound

Lower Bound (>=)	nums[mid] >= target	ans = mid; right = mid - 1	bisect_left
Upper Bound (>)	nums[mid] > target	ans = mid; right = mid - 1	bisect_right
Last Occurrence (<=)	nums[mid] <= target	ans = mid; left = mid + 1	bisect_right - 1