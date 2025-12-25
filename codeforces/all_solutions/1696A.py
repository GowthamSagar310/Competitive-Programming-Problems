for _ in range(int(input())):
    n, z = map(int, input().split())
    arr = list(map(int, input().split()))

    # do operation any number of times >= 0
    
    # choose an element in the array ai 
    # and change it to
    # ai = (ai or z)
    # z = (ai and z)

    # a1 = max(arr), z 
    # a1 = (a1 or z) -> same or value is increased
    # z = (a1 and z) -> same or less

    # if we iterate through all the values of array
    # and choose the one which gives maximum or

    # as for the subsequent operation, z would be equal or less
    
    # case 1
    # if z is equal and there is bigger or giving value, 
    # we would have found it in the first place 

    # case 1 
    # if z is less, how can we prove that there wont be a bigger or giving value ?
    # 
    # say this is a value in the array (which initially did not give maximum or) - > aj
    # we want to see if this aj is going to give more OR value with z_reduced than z_original
    # (IMPORTANT: because z = z AND ai, the bits in z are always equal or less, in this case less.)
    # there ak | z_reduced will always be  <= ak | z_original
    # because the number of bits in z_reduced decreased, ak | z_reduced can never have more bits than ak | z_original 
    # (if yes, that would have been picked)
    # so, the first choosen value is always the maximum
    
    print(max(ai | z for ai in arr))
    