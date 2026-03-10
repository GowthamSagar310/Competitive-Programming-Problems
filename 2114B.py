for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ones = s.count("1")
    zeroes = n-ones

    # n is always even

    # x ones pairs
    # k-x zeros pairs
    # ones - 2 * x = zeros - 2 * (k-x)
    # ones - 2x = zeros - 2k + 2x
    # 2k = zeros - ones + 4x
    # k = (zeroes-ones) // 2 + 2x

    # RHS = fixed.

    if ones == zeroes:
        print("YES")
    else:
        