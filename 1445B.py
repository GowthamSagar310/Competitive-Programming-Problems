for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    """
    1. there are more than 100 participants
    2. two contests. 
    3. atleast 100 people should be moving to the final stage

    3. in first, 100th scored "a", 
    a+x, a+y ......... a a-a1 a-a2 ... 
    6. all the 1-100th place (in second contest) have atleast "d" points 
    
    4. in second contest, 100th scored "c"
    5. all the 1-100th place have atleast b points in the contest
    
    1 2 2 1
    
        
    a = 4 
    b = 8
    c = 9
    d = 2

    in the first contest, 100th scored 4. meaning all the above have >= 4
    these 100 particpants in the second contest, scored atleast 8 points
    so the score of these 100participants must be >= 12 after the two contests.

    in the second contest, 100th scored, 9 points
    these 100 participants in the first contest, scored atleast 2 points. 
    so the score of these 100 participants must be >= 11 after the two contests.
    """

    print(max(a+b, c+d))