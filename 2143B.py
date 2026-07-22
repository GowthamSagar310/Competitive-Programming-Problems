for _ in range(int(input())):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    vouchers = list(map(int, input().split()))
    prices.sort(reverse=True)
    vouchers.sort()
    ptr = 0
    total_cost = 0
    j = 0
    while j < k and ptr < n:
        v = vouchers[j]
        for i in range(v):
            if i != v-1 and ptr < n:
                total_cost += prices[ptr]
            ptr += 1
            if ptr >= n: break
        j += 1
    total_cost += sum(prices[ptr:n])
    print(total_cost)
