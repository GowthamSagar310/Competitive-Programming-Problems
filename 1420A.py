def solve(arr, n):
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            return True
    return False
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    1. maximum swaps doable = (n * (n-1) // 2) - 1
    2. what is the maximum number of swaps any array takes to sort itself in this way ? 
       if the element is out of order with everything on its right, we need to make 
       (number of elements of right - 1) swaps to get that element to right place.

       if every number is out of order, like 5 4 3 2 1
       we need to make the maximum number of swaps

       number of inversions = number of out of order pairs
       (ai > aj and ai is before aj)

       max number of inversions = (n * (n-1) // 2)
       max number of pairs of numbers = nC2 = (n * (n-1) // 2) = max number of inversions an array can have

    3. so if the maximum swaps doable is 1 less than max, we cannot have strictly decreasing array
       because the number of inversions exceed the allowed swaps.

        5, 4, 3, 2, 1  takes 5 * 4 // 2 = 10 swaps
        
        5, 4, 4, 3, 2, 1
        max inversions = 4 + 3 + 3 + 2 + 1 = 14
        doable inversions = (n * (n-1) // 2) - 1 = 6 * 5 // 2 - 1 = 14

        4_A moves to end with 1 swap [4, 5, 4, 3, 2, 1]
        4_B moves to end with 1 swap only (it does need to go over 4_A) [4, 4, 5, 3, 2, 1]
        3 moves 3 [3, 4, 4, 5, 2, 1]
        2 moves 4
        1 moves 5
        total = 5 + 4 + 3 + 1 + 1 = 14
    """

    print("YES" if solve(arr, n) else "NO")