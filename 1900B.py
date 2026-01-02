for _ in range(int(input())):
    a, b, c = map(int, input().split())

    # Case1: for "a"
    # what are the all ways ? 
    # 1. use b, c -> b-c difference changes by 0
    # 2. use a, c -> b-c difference changes by 2
    # 3. use a, b -> b-c difference changes by -2

    # in all the three operations, b-c is changed by even number 
    # to reach a state where b=0 and c=0 (which is even)
    # and with the operations we are only able to reduce by even number
    # so if b-c is odd, we cannot make is 0 ever

    res = [
        (b-c) % 2 == 0,
        (c-a) % 2 == 0,
        (a-b) % 2 == 0
    ]
    print(*map(int, res))
