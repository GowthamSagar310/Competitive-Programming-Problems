def solve(nums):
    maxi = 10**5 # if this is bigger, it might cause MLE
    divisors = [[1, 1] for _ in range(maxi+1)]
    for i in range(2, maxi+1):
        for j in range(i, maxi+1, i):
            divisors[j][0] += i
            divisors[j][1] += 1
    res = 0
    for n in nums:
        if divisors[n][1] == 4: print("num", n)
        res += divisors[n][0] if divisors[n][1] == 4 else 0
    return res

nums = list(range(1, 101))
solve(nums)


# 6 = 1, 2, 3, 6
# 8 = 1, 2, 4, 8
# 10 = 1, 2, 5, 10
# 14 = 1, 2, 7, 14
# 15 = 1, 3, 5, 15