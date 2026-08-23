for _ in range(int(input())):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))

    """
    let x, y be the numbers

    if they are choose individualy 
    total score added = x + y - 2c
    if as a pair = max(x, y)-c

    what is the gain from choosing pair over individual values ? 
    = max(x, y) - c -x - y + 2c
    = c - min(x, y)

    if we can decrease the min(x, y), then we can increase the gain
    = so which pairs (x, y) to choose ?

    - how many pairs of (x, y) can be choosen ? floor(n // 2)
    - minimum elements must be next to some element which is same or bigger
    - [3, 1, 4, 1, 5, 9]
    - here the first n // 2 small numbers are  [1, 1, 3] [4, 5, 9]

    - the pairs an (1, 4) (1, 5) (3, 9)
    - the pairs can also be (4, 1) (1, 5) (3, 9)

    there is always a way to select these such that the min(x, y) is in first n // 2 elements

    - over the individual values, if c > min(x, y) there is always gain
    - but if c <= min(x, y) then there is no gain, we need to stop

    """

    total = sum(arr) - n * c
    arr.sort()
    gain = 0
    for i in range(n // 2):
        if arr[i] >= c:
            break
        gain += (c - arr[i])
    print(total + gain)