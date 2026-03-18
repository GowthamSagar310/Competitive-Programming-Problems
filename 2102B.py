def solve(arr):
    """
    1.  we need to know if there are k = (n-1) // 2 elements before the arr[0] (after sorting)
        either negative or positive value
    2.  when arr[0] is choosen as positive (original value without flipping)
        we need to check how many absolute values are smaller and larger than the arr[0]
        S, L be the counts of it. 

        why are we checking for absolute values ? instead of original values ? 
        -> -4 < 10, 4 < 10 if absolute value is less than target, then flipping does not matter in this case
        -> -15 < 10, 15 > 10 if absolute is greater than target, then flipping changes the side from greater to smaller
        -> so if there are S smaller values and L larger values, we can flip larger values to the other side to make the required "k" count
        -> if there are no enough larger values, then we cannot make it. 
        -> if there are more smaller values than k, we can never flip the smaller values. so we cannot make it. 
        -> so basically, we need k <= s + l and also k >= s

    3. but what the target is negative of the original value ? 
        -> -6 < -5, 6 > -5 if the absolute value is greater than the negative target, then flipping changes the sides
        -> -4 > -5, 4 > -5 if the absolute value is lesser than the negative target, then flipping does not matter. 
        -> so larger values matter here.
        -> if there are enough larger values, then we can flip the sides
        -> k <= larger 
    """

    k = (n-1) // 2
    target = abs(arr[0])
    less = more = 0
    for i in range(1, n):
        if abs(arr[i]) < target:
            less += 1
        else:
            more += 1

    return (less <= k <= less + more) or k <= more
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr) else "NO")
