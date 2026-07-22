from math import lcm
for _ in range(int(input())):
    a, b, c, m = map(int, input().split())


    """
    a, 2a, 3a, ....
    b, 2b, 3b, ....
    c, 2c, 3c, ....

    a = 2, b = 1, c = 3

    lcm(a, b) = 2
    lcm(b, c) = 3
    lcm(a, c) = 6
    lcm(a, b, c) = 6

    - for every multiple of 6, we will only get 2 litres = 10 // 6 = 1
    - for every multiple of 3, excluding multiples used above = 
        - if curr % prev == 0, then there will be some overlap
        - how many multiples are same ? 
        - multiples of smaller number - mulitples of bigger
        - (10 // 3) - 1
        - 2
    - 

    14 35 5

    1 2 3 4 5 6 7 8 9 10

    6 = 1
    3, 9 = 2
    2, 4, 8, 10 = 4
    1, 5, 7 = 3

    """

    ans = [0, 0, 0]
    multiples = [0] * 7
    lcms = [
        [a, "a"],
        [b, "b"],
        [c, "c"],
        [lcm(a, b), "ab"],
        [lcm(b, c), "bc"],
        [lcm(c, a), "ca"],
        [lcm(a, b, c), "abc"]
    ]
    
    for i in range(6, -1, -1):
        l, s = lcms[i]
        ml = m // l
        same_ml = 0
        for j in range(i+1, 7):
            if lcms[j][0] % l == 0:
                same_ml += multiples[j]

        # remove already used multiples
        ml -= same_ml
        multiples[i] = ml
        if ml:
            for c in s:
                ans[ord(c)-ord('a')] += ml * (6 // len(s))
    print(*ans)