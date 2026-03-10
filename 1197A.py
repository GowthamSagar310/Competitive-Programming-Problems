for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    """
    
    1. all the values are >= 1 based on input constraints
    2. so n-2 planks can be used for steps
    3. to maximize the base planks, we choose maximum two values
       = min(arr[-1], arr[-2])-1
       = which is just, arr[-2]-1
    4. what if arr[-2]-1 > n-2 ? meaning we dont have arr[-2]-1 planks
       then we reduce the k to n-2. since this is always possible.
       we already have 2 atleast k+1 planks
    5. what if arr[-2]-1 < n-2 ? we have lot more steps, but limited by base plank's size
    """

    print(min(n-2, arr[-2]-1))