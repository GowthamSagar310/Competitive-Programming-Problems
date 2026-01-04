for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    a AND b >= a XOR b

    if the largest set bit in a, b is at same position, a & b >= a ^ b
    this is always true. 
    if it is not the same pos, then it wont work. 

    how many pairs ? 
    if there are 10 numbers with same pos, 10C2 pairs

    """

    freq = {}
    for num in arr:
        pos = 0
        while num:
            pos += 1
            num >>= 1
        freq[pos] = freq.get(pos, 0) + 1

    total = 0
    for v in freq.values():
        if v > 1:
            total += (v * (v-1)) // 2
    print(total)
