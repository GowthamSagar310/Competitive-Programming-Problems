for _ in range(int(input())):
    n = int(input())
    s = input()

    """
    - choose d 
    - t = right shift s by d
    - s = t or s
    - make all 1s in s

    - this is same as the longest consecutive zeros (cyclic) 
    - because every bit has to be 1
    - with d = 1, everything on the right of "1" can be made 1.
    - we keep doing this and at last, the only that might remain is the longest consecutive zeroes section
    - which also takes d (remaining zeroes) steps
    """
    longest = 0
    count = 0
    for i in range(2*n): # this calculation works because there is atleast one "1". so the loop breaks without double counting for case where all are zeroes.
        if s[i % n] == "0":
            count += 1
            longest = max(longest, count)
        else:
            count = 0
    print(longest)
