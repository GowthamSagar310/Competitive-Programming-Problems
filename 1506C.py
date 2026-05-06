for _ in range(int(input())):
    a = input()
    b = input()

    # longest common substring of a in b 
    # a being the smallest and b being largest
    
    if len(a) > len(b):
        a, b = b, a

    maximum = 0
    for i in range(len(a)):
        for j in range(len(b)):
            count = 0
            temp_i = i
            while temp_i < len(a) and j < len(b) and a[temp_i] == b[j]:
                j += 1
                temp_i += 1
                count += 1
            maximum = max(maximum, count)
    print(len(a) + len(b) - 2 * maximum)
