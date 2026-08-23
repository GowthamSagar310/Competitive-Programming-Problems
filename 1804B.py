for _ in range(int(input())):
    n, k, d, w = map(int, input().split())
    arr = list(map(int, input().split()))
    # original_k = k
    # packs = 0
    # i = 0
    # while i < n:
    #     pack_open = arr[i]+w
    #     pack_expire = pack_open+d
    #     packs += 1
    #     while i < n and arr[i] <= pack_expire:
    #         if not k:
    #             pack_open = arr[i]+w
    #             pack_expire = pack_open+d
    #             k = original_k
    #             packs += 1
    #         k -= 1 
    #         i += 1
    #     k = original_k
    # print(packs)

    ans = 0
    i = 0
    while i < n:
        ans += 1
        rem = k
        expire = arr[i]+w+d
        while i < n and rem > 0 and arr[i] <= expire:
            rem -= 1
            i += 1
    print(ans)
