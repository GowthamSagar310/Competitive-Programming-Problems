for _ in range(int(input())):
    n, k = map(int, input().split()) # k is always 1
    arr = list(map(int, input().split()))
    p = int(input()) # 1 based index
    x = arr[p-1]

    """
    - k is always
    - need to choose a range [l, r] which includes "p" always
    - flip all the bits in that range
    - atlast make all the bits of the arr = x
    - find the minimum number of operations

    0 1 0 '1' 0 1
    
    flip=1    0 1 0 0 0 1
    flip=2    0 1 1 1 0 1
    flip=3    0 0 0 0 0 1
    flip=4    1 1 1 1 1 1

    0 1 1 0 '1' 1 0 1 0 0 1 0 1 0 1 0 1
    
    flip=1  0 1 1 0 0 1 0 1 0 0 1 0 1 0 1 0 1
            0 1 1 1 1 1 0 1 0 0 1 0 1 0 1 0 1
            0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 0 1
    
    """
    def expand(curr, l, r):
        while l-1 >= 0 and curr == arr[l-1]:
            l -= 1
        while r+1 < n and curr == arr[r+1]:
            r += 1
        return [l, r]
    curr = x
    flips = 0
    l, r = expand(curr, p-1, p-1)
    while r-l+1 != n:
        flips += 1
        curr = 1-curr
        l, r = expand(curr, l, r)
    if curr != x: flips += 1
    print(flips)
