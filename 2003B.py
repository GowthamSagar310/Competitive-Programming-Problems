for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    turtle: remove smallest values 
    piggy: remove biggest values

    turtle's strategy is to remove the smallest values from the array,
    so that the changes of maximizing the value increases. 
    smallest number must be adjacent to some number (bigger or same)
    so, we can always remove the one of the smallest number
    2 1 - one can be removed max(2, 1) = 2, remove 1
    1 2 - one can be removed max(1, 2) = 2, replace 1 with 2, remove 2

    so always a smallest number of removed. 
    similarily we can do the same for biggest numbers for piggy.

    we can removing from the both the ends of the sorted array
    and we will be left with one value at the end.

    1 2 2 3 3
    1 3 5 4 2
    
    1 2 2 3 3 3
    1 3 5 6 4 2

    the games stops when there is only one value

    even length -> odd (1) takes odd steps -> turtle played his chance, so he picked max value of two
    odd length -> odd (1) takes even steps -> piggy played his chance, so he picked min value of two
    """

    arr.sort()
    # choosing the middle element or the second middle element in case of even lengthed.
    print(arr[n//2])