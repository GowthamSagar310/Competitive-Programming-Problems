for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ans = ["+"] * n
    """
    
    0 - remove top
    1 - remove bottom
    2 - remove either top or bottom

    0, 1 are deterministic
    2 effects 

    - if the remove the cards in the order 001001 or 000011
    - the number of cards removed and the cards which are removed will always be same
    - at the end of all operations, we are removing 4 top cards for sure and 2 bottom cards for sure 

    - if are doing "2" kind of operation, we are not certain where top is removed or bottom. 
    - 0222201111212121
    - for this, in the end of the operations, for sure, the first two cards should have been removed. 
    - even if "2" are done on all the bottom side, the second top card must be removed. 



    - for these kinds of problems we need to see if the order of the operations matter. 
    - minimum_number of top cards removed = count("0")
    - minimum_number of bottom cards removed = count("1")
    - for "2" operations, either a top or bottom will be removed.
    - max_top that can be removed = count("0") + count("2")
    - max_top that can be removed = count("1") + count("2")

    [min_top, max_top]
    [min_bottom, max_bottom]
    
    if pos is <= min_top: definitely removed
    if pos is >= min_bottom: definitely removed
    if max_top < pos < max_bottom: wont be able to touch
    
    if min_top < pos <= max_top: cant be said
    if max_bottom <= pos < min_bottom: cant be said
     
    """

    if k == n:
        # there are n operations performed and each op removed one card, so all cards must be gone. 
        print("-" * n)
        continue

    min_top = s.count("0")
    min_bottom = s.count("1")
    gap = s.count("2")
    ans = ["?"] * n

    for i in range(1, n+1):
        distance_from_bottom = n-i+1
        if i <= min_top or distance_from_bottom <= min_bottom: ans[i-1] = "-"
        elif i > (min_top + gap) and distance_from_bottom > (min_bottom + gap): ans[i-1] = "+"
    
    print("".join(ans))
 