for _ in range(int(input())):
    n = int(input())

    """
    1. if he has to get any cashback, x >= 10
    2. 10//10, 11//10, 12/10 ... 19//20
       all give the same cashback. so why waste more coins ? 
       use only 10, get cashback 1

    3. this problem is so similar to 1352C, 460A
       1. it is always best to use 10 multiples as explained above
       2. think of spending 1 coin each day for 10 days, instead all 10 at once. 
          so, on the 10th day, say 1 use one coin, 1 gain one back. so the net is 0
          so, 10th day is counted, meaning numbers which are divisible by 10 are not counted. 
          so to fit n=22 coins into 9 day groups (because 10th day is skipped.)

          total rows needed = ceil(n/9)
          number of days divisible by 10 to skip = total rows - 1
          = ceil(n/9)-1
          = floor(n+9-1 / 9) -1
          = floor(n+9-1-9 / 9)
          = floor(n-1 / 9)
          = total cashback received.
       
    """

    print(n + (n-1) // 9)