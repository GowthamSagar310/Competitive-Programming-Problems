for _ in range(int(input())):
    n = int(input())

    """
    6,   8, 10
    15, 20, 25

    15/6 = 2.5
    20/8 = 2.5
    25/10 = 2.5

    for each slice is takes the same amount. 
    so it does not matter which combination I choose.

    1. if n is odd, I have to choose n+1. because 6,8,10 are even, I cannot make an odd sum. 
    2. if n is even, I need to check if I can always find a combination of a,b,c to sum up for N
       if we can prove that there always exists a combination, a, b, c, then answer is just N * 2.5
       because to make each slice it takes the same amount of time 2.5


       I need to prove that for all even numbers n >= 8, there exists non-negative a,b,c
       such that 6a + 8b + 10c = n

       considering mod 6 (r can only be 0, 2, 4 since n is even)
       
       case1: n % 6 == 0 -> (a = n // 6, b = 0, c = 0)
       
       case2: n % 6 == 2
       -> reduce one 6 and use that in addition with remainder 2 = 6+2 = one 8 
       -> k = n // 6
       -> a = k-1, b = 1, c = 0

       case3: n % 6 == 4
       -> reduce one 6 and use that in addition with remainder 4 = 6+4 = one 10 
       -> k = n // 6
       -> a = k-1, b = 0, c = 1

       in all three cases, there is a valid (a, b, c) combination. so all even numbers >= 10 should be possible


       NOTE 1: 6, 8, 10 all share a common factor of 2. so their combinations also share 2, which means only even numbers can be made
       NOTE 2: 3, 4, 5 do not share. so even and odd are possible. but what are all the numbers that we can make with 3, 4, 5 ? 
               by the similar logic used above, every number >= 5

    """

    if n < 6: 
        print(15)
        continue

    if n & 1: n += 1
    print((n * 5) // 2)

    # be careful here. int(n * 2.5) causes errors due to precision issues with large numbers