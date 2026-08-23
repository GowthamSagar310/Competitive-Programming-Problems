for _ in range(int(input())):
    a, b, m = map(int, input().split())
    if a > b: a, b = b, a
    """
    [6,10], 12, 18, 24 ......
    [7,11], 14, 21, 28 ......
    
    [3,13], [6,16], [9, 19] [12,22]....
    [4,14], [8,18], [12,22] ....

    7 14 21 28 35 42 49 56 63 70
    [7, 63], [14, 70], [21, 77] ....


    8 16 24 32 40 48 56 64
    [8, 64], [16, 72], [24, 80] ....

    
    interval here is [a, a+m]
    how many multiples of a fit inside this ? 
    gaps = (distance)//a 
    gaps = (m)//a
    values = gaps + 1 (points) = m//a + 1

    for b, [b, b+m]
    values = m//b + 1

    - since m, is same for both. 
    - we need to find time "t" such that both maximums are possible 
    - t = lcm(a, b) -> why ? 

    the maximum values for "a" are possible when ? 
    when the time is divisible by 'a', so we are not wasting any space.
    [5, 15] -> [5, 10, 15]
    [6, 15] -> [10, 15]
    [5, 14] -> [5, 10]

    t - m % a == 0 
    t % a == 0

    same goes for b.
    t - m % b == 0
    t % b == 0

    if t is divided by both     

    """