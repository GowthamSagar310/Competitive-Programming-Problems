for _ in range(int(input())):
    n, m, k = map(int, input().split())
    for i in range(n-m): print(n-i, end = " ")
    for i in range(m): print(i+1, end = " ")
    print()
    
    # f(i) - g(i)
    # f(i) is looking for >= k
    # it is optimal to keep bigger numbers at the front because
    # they contribute to the prefix sums multiple times
    # bigger to smaller (n-m) values

    # g(i) is looking for <= m
    # it is optimal to have smaller numbers contribute more times than bigger numbers
    # so, smaller to bigger (m) values

    # why cant we have bigger to samller k values ? 
    # it has to be permutation, all numbers must be present.