for _ in range(int(input())):
    n = int(input())
    s = list(input())


    """
    - we need to properly identify the sections of zeros
    - each 1 can block three places. itself, left and right
    - cases
    - 1. prefix_zero_section (only right boundary has 1)
    - 2. middle_zero_section (both boundaries have 1s)
    - 3. suffix_zero_section (only left boundary has 1)

    - to make it easier, we converting everything into middle
    - by assuming there are ghost 1s before 0 and after n-1 indexes
    - by assuming 1 at -2, we are essentially free to add 1 at 0 index
    - by assuming 1 at n+1, we are essentially making it legal to add 1 at n-1 index
    
    """

    last_seen_one = -2 # assuming a phanton. 
    original_ones = 0
    added_ones = 0
    for i in range(n):
        if s[i] == "1":
            gap = (i-1) - (last_seen_one+1) +1
            original_ones += 1
            added_ones += gap // 3
            last_seen_one = i
    
    # for the last part, if there are zeros
    gap = n-(last_seen_one+1)+1
    added_ones += gap // 3
    print(added_ones + original_ones)
    
            
    