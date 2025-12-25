for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # this is good problem. 

    o_count = sum(a & 1 for a in arr)
    e_count = n - o_count

    if o_count:

        # if there is atleast one odd number
        # we can fuse that with even number and form a new odd
        # it is like eating away all even numbers

        print(e_count)
    else:

        # if everything is an even number
        # then we need to create atleast one odd number and then eat away evens

        def get_ops(x):
            ops = 0
            while x % 2 == 0:
                ops += 1
                x //= 2
            return ops

        ops = min(get_ops(a) for a in arr)
        ops += e_count - 1 # remaining even number can be fused

        print(ops)