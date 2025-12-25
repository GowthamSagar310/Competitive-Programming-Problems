def solve(arr):
    total = sum(arr)
    left = 0 
    for l in range(n-1):
        left += arr[l]
        middle = 0
        for r in range(l+1, n-1):
            middle += arr[r]
            right = total - (left + middle)
            s1 = left % 3
            s2 = middle % 3
            s3 = right % 3

            # in python a == b == c is evaluated as (a == b) and (b == c) -> meaning a == b == c (as if a == b and b == c -> a == c)
            #           a != b != c is evaluated as (a != b) and (b != c) -> which does not translate to a != b != c, it does not check for a != c
            #           a < b < c is evaluated as (a < b) and (b < c) -> meaning a < b < c (as if a < b and b < c -> a < c)
            # transitive property:  if a op1 b and b op1 c then a op1 c is true

            # if (
            #     (s1 == s2 and s2 == s3 and s3 == s1) or 
            #     (s1 != s2 and s2 != s3 and s3 != s1)
            # ):
            #     return [l+1, r+1]

            if len({s1, s2, s3}) in (1, 3):
                return [l+1, r+1]
    return [0, 0]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solve(arr))