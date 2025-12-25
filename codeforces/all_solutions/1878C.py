for _ in range(int(input())):
    n, k, x = map(int, input().split())

    # k distinct integers between 1 and n to sum up to x
    # max sum = (n * (n + 1)) // 2

    minimum_possible = (k * (k + 1)) // 2
    total_sum = (n * (n+1)) // 2
    d = n-k # first n-k elements
    first_d_sum = (d * (d+1)) // 2
    maximum_possible = total_sum - first_d_sum
    print("YES" if minimum_possible <= x <= maximum_possible else "NO")

    # how do we prove this ? 