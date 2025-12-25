for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split())) 
    ones, zeroes = 0, 0
    for num in arr:
        ones += 1 if num == 1 else 0
        zeroes += 1 if num == 0 else 0
    
    # if there are no zeroes, and k ones 
    # there are k combinations (by removing different 1 in each combination)

    # now if there are x zeroes, and k ones
    # there are k combinations from ones 
    # for each of these combinations,
    # we have 2^x combinations of zeros

    print(ones * (2 ** zeroes))


