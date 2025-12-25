for _ in range(int(input())):
    s = input()

    # 00001111
    # largest index of 0 < smallest index of 1
    # if min(0 count, 1 count) -> odd -> DA

    # 11110000
    # largest index of 0 < smallest index of 0
    # if min(0 count, 1 count) -> odd -> DA
    
    # 010110010
    # these will in some way be cancelled out
    # meaning there is always a possibility of 0 next 1
    # so, it is just minimum number of 0 or 1 

    # as long as there are 0 and 1 in the string
    # there must be a boundary at which they touch

    one_count = s.count("1")
    zero_count = len(s) - one_count
    mini = min(one_count, zero_count)
    if mini & 1:
        print("DA")
    else:
        print("NET")

