for _ in range(int(input())):
    n = input()

    """
    102030 = (03 / 3 + 0) = 1
    """ 

    # l = len(n)
    # i = l-1
    # zeros = 0
    # while i >= 0 and n[i] == "0":
    #     zeros += 1
    #     i -= 1
    
    # non_zeros = 0
    # for j in range(i-1, -1, -1):
    #     if n[j] != "0":
    #         non_zeros += 1

    # print(zeros + non_zeros)

    l = len(n)
    i = l-1
    while i >= 0 and n[i] == "0": i -= 1
    print((i-n[:i].count("0")) + n[i+1:].count("0"))