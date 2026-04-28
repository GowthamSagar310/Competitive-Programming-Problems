from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    """
    - we have to always add to the end of the chain. 
    - so find the largest chain. (1, 2, 3, ... k numbers)
    - numbers can be choosen and then added in sorted fashion. 
    """

    # so basically, we need to look which group is breaking the whole thing apart. 
    # it is not in order within itself

    m = {val: index for index, val in enumerate(arr)}
    val = 1
    prev_index = -1
    groups = 0
    for _ in range(n):
        index = m[val]
        if index < prev_index:
            elements_to_move = n-val+1
            groups = ceil((n-val+1) / k)
            break
        val += 1
        prev_index = index
    print(groups)