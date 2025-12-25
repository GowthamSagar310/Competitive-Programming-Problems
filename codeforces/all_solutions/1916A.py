# 2023
# divisors ? 
# 1, 7, 17, 7 * 17, 17 * 17, 2023

# if the numbers in b are not dividing 2023, NO

import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    prod = math.prod(arr)
    if 2023 % prod:
        print("NO")
    else:
        print("YES")
        print(str(2023 // prod) + " " + "1 " * (k-1))
