for _ in range(int(input())):
    n = int(input())
    # jars = n

    # 2kg berries -> 3 kg jam
    # 1 jar -> 3kg jam -> 2kg berries
    # n jar -> 3 * n jam -> 4kg berries

    print(2 * n)
