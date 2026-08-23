for _ in range(int(input())):
    n = int(input())
    s = input()
    """
    1. objective: make the string alternating in minimum number of ops
    2. rules: 
        - the deleted character sequence must be alternating
        - first character can be 0 or 1
    
    
    abs(f0-f1) <= 1
    abs(r0-r1) <= 1
    
    """

    m0 = s.count("0")
    m1 = n - m0

    if abs(m0-m1) > 2:
        print(-1)
        continue

    c0 = c1 = 0
    for i in range(1, n):
        if s[i] == s[i-1]:
            if s[i] == "0":
                c0 += 1
            else:
                c1 += 1

    if abs(c0-c1) <= 1:
        print(c0 + c1)
    else:
        print(2 * max(c0, c1) - 1)
