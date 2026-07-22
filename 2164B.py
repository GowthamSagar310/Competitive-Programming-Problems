for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    """
    
    - strictly increasing. so distinct
    - choose two numbers from the array, such that
    - x < y and y mod x = even


    can there be a combination of even and odd number ? not possible
    assume x = even, y = odd and both are != 1
    x = 2k1
    y = 2k2 + 1
    y / x = (2k2 + 1) / 2k1
    k4 + 2k3 = (2k2 + 1) / 2k1
    
    2k1k4 + 4k3k4 = 2k2 + 1
    even = odd 
    not possible


    can there be a combination of odd and even number ? possible
    x = odd, y = even

    x = 2k1 + 1
    y = 2k2

    y / x = 2k2 / 2k1 + 1

    k4 + 2k3 = 2k2 / 2k1 + 1
    2k1k4 + k4 + 4k1k3 + 2k3 = 2k2
    k4 has to be even
    
    even, even case always works

    odd, odd case
    y mod x = even
    y - qx = even
    odd - q. odd = even
    - q. odd has to be odd
    - q has to be odd

    - but to find the pairs which have this property is O(N ** 2) on odd array
    - so we need to ask differnt question here. 

    - when is it certain that there is no answer
    - for the evens case, there is should atmost only 1 even number
    - for the odds case, y mod x should odd to not have a solution
    y mod x = odd
    y - qx = odd
    odd - q. odd = odd
    q.odd must be even
    q must be even

    x < y, y // x >= 1 = q
    q >= 1, and also q must be even
    so q >= 2

    which means
    y // x >= 2
    y >= 2x (to not have a solution, y >= 2x and q is even)

    but arr[i] <= 10^9
    so to not have any valid pair, every odd number should be twice as large as previous number 

    1 3 7 15 31 

    2 ^ n < 10^9

    2^10 ~ 10^3
    2^30 ~ 10^9

    so after 30 doubling of the double numbers, we would reach a number which is > 10^9
    which according to the question is not possible. 

    so for the array to have no valid pairs, it cannot have more than 30 elements.
    so if there are more than 30 elements, there might be answer possible.

    let odds be
    a1, a2, a3 .....

    a2 < 2 * a1 then a2 mod a1 = a2 - a1 = odd - odd = even !! 
    
    if a2 >= 2 * a1, then a2 mod a1 = some 0 < r < a1 which might be even or not. 
    if we keep going like this, 

    a2 >= 2 * a1
    a3 >= 2 * a2
    ...

    this can go only log2(max_value) times, which is in this ~30
    so if in the first 30 elements, there must be an answer.

    
    """
    n = min(n, 30)
    found = False
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] % arr[i] % 2 == 0:
                print(arr[i], arr[j])
                found = True
                break
        if found: break
    if not found:
        print(-1)
    
