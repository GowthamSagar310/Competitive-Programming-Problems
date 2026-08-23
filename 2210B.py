for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    - the idea here is,
    - if the value is pointing to a forward chair, we are guaranteed to loose or end prematurely. 
    - but if the value is pointing backwards, it always safe and we are effecting any future chances.
    - so if we can keep playing safe, without triggering any forward values, 
    - we are bound to sit on all the safe chairs and 
    - if there is a strategy which involves marking a chair in future, 
    - it should always <= safe chairs because we are cutting in between and only moving from left to right
    """

    count = 0
    for i in range(n):
        if arr[i] <= i+1:
            count += 1
    print(count)