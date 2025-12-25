from collections import defaultdict

n = int(input())
arr1 = list(map(int, input().split())) # strictly increasing + unique

m = int(input())
arr2 = list(map(int, input().split())) # strictly increasing + unique

# requirement 1 
# gear ratio (arr2 / arr1) must be an integer

# requirement 2 
# maximum ratio

# it is guaranteed that atleast one integer gear ratio exists

# for every number in arr2
#   - check if divisor exists in arr1
#   - store the maximum

ratios = defaultdict(int)
max_ratio = 0
for num2 in arr2:
    for num1 in arr1:
        if num2 % num1 == 0:
            ratios[num2 // num1] += 1
            max_ratio = max(max_ratio, num2 // num1)
print(ratios[max_ratio])