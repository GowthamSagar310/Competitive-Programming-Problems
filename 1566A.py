for _ in range(int(input())):
    n, s = map(int, input().split())

    # median -> middle element of non decreasing order 
    # non-negative integers include 0

    index = (n // 2) + (n % 2) # 1 based index
    index -= 1

    # 0 0 0 0 x x x x x x

    # left_terms = (index-1-0+1)
    right_terms = (n-1-index+1)

    # left_terms * 0 + right_terms * x = s
    x = s // right_terms

    # observe that, if s % right_terms != 0
    # then, say s % right_terms = r 
    # this r will always be less than right_terms
    # which is the case with median, so (index-1) term will always be there if r != 0
    # so, r can be added in index-1 position

    print(x)
