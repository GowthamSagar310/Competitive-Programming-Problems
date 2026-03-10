n = int(input())
curr = 0
for _ in range(n):
    s, d = map(int, input().split())
    if curr < s:
        curr = s
    else:
        """

        curr = 6
        s, d = 3, 3

        3 + 3 * (5 // 3)
        """

        curr = s + d * (((curr - s) // d) + 1)
print(curr)

"""
ceil(a/b) = floor(a+b-1/b)
"""